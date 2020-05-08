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
    query = "SELECT * FROM `kucoin`.`ethusdt` ORDER BY `record_time` ASC LIMIT 7000"  # HAS TO BE ASCENDING ORDER
    df = pd.read_sql(query, con)

    # calculating spread and midprice
    df["spread"] = df["ask1_price"] - df["bid1_price"]
    df["midprice"] = (df["ask1_price"] + df["bid1_price"]) / 2.0

    # calculating momentum
    df["momentum-15"] = df["midprice"] - df["midprice"].shift(15)

    # calculating OBV
    vols = [name for name in list(df.columns) if "_vol" in name]
    df["vol"] = df[vols].sum(axis=1)
    df["OBV"] = -1614347.8061
    for i in range(1, len(df)):
        if df.loc[i, "midprice"] > df.loc[i - 1, "midprice"]:
            df.loc[i, "OBV"] = df.loc[i - 1, "OBV"] + df.loc[i, "vol"]
        elif df.loc[i, "midprice"] < df.loc[i - 1, "midprice"]:
            df.loc[i, "OBV"] = df.loc[i - 1, "OBV"] - df.loc[i, "vol"]
        else:
            df.loc[i, "OBV"] = df.loc[i - 1, "OBV"]

    # comparing midprice to the future midprice in 5 rows
    df["time_diff"] = df["record_time"].shift(-5) - df["record_time"]
    df["time_diff"] = df["time_diff"] / np.timedelta64(1, "s")
    df["movement"] = (
        (df["midprice"].shift(-5) - df["midprice"]) > (df["midprice"] * FEE)
    ) * 1  # converting a serie of bool to a serie of int

    df = df.drop(columns=["spread", "record_time", "time_diff", "vol"])

    df = df.dropna()
    output_arr = []

    # pd.set_option("display.max_rows", None)
    # print(df)

    for i in range(len(df)):
        pair = {
            "price": df.iloc[i].values[:-1].tolist(),
            "class": str(df.iloc[i, -1]),
        }
        output_arr.append(pair)

    # print(output_arr)

    output_file_path = "./train.json"
    with open(output_file_path, "w") as f:
        json.dump(output_arr, f)

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
