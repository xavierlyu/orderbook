import pandas as pd
import numpy as np
import pymysql
import json
import matplotlib.pyplot as plt

config_file_path = "./config.json"

with open(config_file_path, "r") as handler:
    config = json.load(handler)

FEE = float(config["exchange"]["fee"])

host = config["database"]["host"]
port = int(config["database"]["port"])
user = config["database"]["user"]
password = config["database"]["password"]
database = config["database"]["database"]

con = pymysql.connect(host, user=user, port=port, passwd=password, database=database)

with con:
    query = "SELECT * FROM `kucoin`.`ethusdt` ORDER BY `record_time` ASC LIMIT 25"  # HAS TO BE ASCENDING ORDER
    df = pd.read_sql(query, con)

    # bid-ask spreads, mid-prices, and price differences
    for l in range(1, 11):
        df[f"spread_{l}"] = df[f"ask{l}_price"] - df[f"bid{l}_price"]
        df[f"midprice_{l}"] = (df[f"ask{l}_price"] + df[f"bid{l}_price"]) / 2.0

        if l > 1:
            df[f"ask_diff_{l}"] = df[f"ask{l}_price"] - df["ask1_price"]
            df[f"bid_diff_{l}"] = df["bid1_price"] - df[f"bid{l}_price"]

    # mean prices and volumes
    vols = [name for name in list(df.columns) if "_vol" in name]
    prices = [name for name in list(df.columns) if "_price" in name]
    ask_prices = [name for name in prices if "ask" in name]
    bid_prices = [name for name in prices if "bid" in name]
    ask_vols = [name for name in vols if "ask" in name]
    bid_vols = [name for name in vols if "bid" in name]

    df["avg_ask_price"] = df[ask_prices].mean(axis=1)
    df["avg_bid_price"] = df[bid_prices].mean(axis=1)
    df["avg_ask_vol"] = df[ask_vols].mean(axis=1)
    df["avg_bid_vol"] = df[bid_vols].mean(axis=1)

    # accumulated differences
    df["acc_price_diff"] = 0
    df["acc_vol_diff"] = 0
    for l in range(1, 11):
        df["acc_price_diff"] = (
            df["acc_price_diff"] + df[f"ask{l}_price"] - df[f"bid{l}_price"]
        )
        df["acc_vol_diff"] = df["acc_vol_diff"] + df[f"ask{l}_vol"] - df[f"bid{l}_vol"]

    # calculating OBV
    df["vol"] = df[vols].sum(axis=1)
    df["OBV"] = -1614347.8061
    for i in range(1, len(df)):
        if df.loc[i, "midprice_1"] > df.loc[i - 1, "midprice_1"]:
            df.loc[i, "OBV"] = df.loc[i - 1, "OBV"] + df.loc[i, "vol"]
        elif df.loc[i, "midprice_1"] < df.loc[i - 1, "midprice_1"]:
            df.loc[i, "OBV"] = df.loc[i - 1, "OBV"] - df.loc[i, "vol"]
        else:
            df.loc[i, "OBV"] = df.loc[i - 1, "OBV"]

    # comparing midprice to the future midprice in 5 rows
    df["time_diff"] = df["record_time"].shift(-5) - df["record_time"]
    df["time_diff"] = df["time_diff"] / np.timedelta64(1, "s")
    df["movement"] = (
        (df["midprice_1"].shift(-5) - df["midprice_1"]) > (df["midprice_1"] * FEE)
    ) * 1  # converting a serie of bool to a serie of int

    df = df.drop(columns=["record_time", "time_diff", "vol", "OBV"])

    df = df.dropna()
    output_arr = []

    pd.set_option("display.max_rows", None)
    print(df)

    # for i in range(len(df)):
    #     pair = {
    #         "price": df.iloc[i].values[:-1].tolist(),
    #         "class": str(df.iloc[i, -1]),
    #     }
    #     output_arr.append(pair)

    # print(output_arr)

    # output_file_path = "./train.json"
    # with open(output_file_path, "w") as f:
    #     json.dump(output_arr, f)

    # fig, ax1 = plt.subplots()
    # color = "tab:red"
    # ax1.set_xlabel("time")
    # ax1.set_ylabel("price ($)")
    # ax1.plot(df["record_time"], df["midprice"], color=color)

    # ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    # color = "tab:blue"
    # ax2.set_ylabel("OBV", color=color)  # we already handled the x-label with ax1
    # ax2.plot(df["record_time"], df["OBV"], color=color)
    # ax2.tick_params(axis="y", labelcolor=color)

    # fig.tight_layout()  # otherwise the right y-label is slightly clipped
    # plt.show()
