import pandas as pd
import numpy as np
import pymysql
import json
import itertools
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm

if len(sys.argv) == 1:
    print("you need to input a number (in minutes)")
    sys.exit(0)

tbar = tqdm(total=140, file=sys.stdout)

v1 = [
    "ask1_price",
    "ask1_vol",
    "bid1_price",
    "bid1_vol",
    "ask2_price",
    "ask2_vol",
    "bid2_price",
    "bid2_vol",
    "ask3_price",
    "ask3_vol",
    "bid3_price",
    "bid3_vol",
    "ask4_price",
    "ask4_vol",
    "bid4_price",
    "bid4_vol",
    "ask5_price",
    "ask5_vol",
    "bid5_price",
    "bid5_vol",
    "ask6_price",
    "ask6_vol",
    "bid6_price",
    "bid6_vol",
    "ask7_price",
    "ask7_vol",
    "bid7_price",
    "bid7_vol",
    "ask8_price",
    "ask8_vol",
    "bid8_price",
    "bid8_vol",
    "ask9_price",
    "ask9_vol",
    "bid9_price",
    "bid9_vol",
    "ask10_price",
    "ask10_vol",
    "bid10_price",
    "bid10_vol",
]


v2 = []
for l in range(1, 11):
    v2.append(f"spread_{l}")
    v2.append(f"midprice_{l}")

v3 = []
for l in range(2, 11):
    v3.append(f"ask_diff_{l}")
    v3.append(f"bid_diff_{l}")

v4 = ["avg_ask_price", "avg_bid_price", "avg_ask_vol", "avg_bid_vol"]

v5 = ["acc_price_diff", "acc_vol_diff"]

v6 = [
    "ask1_price_ddx",
    "bid1_price_ddx",
    "ask1_vol_ddx",
    "ask2_price_ddx",
    "bid2_price_ddx",
    "ask2_vol_ddx",
    "ask3_price_ddx",
    "bid3_price_ddx",
    "ask3_vol_ddx",
    "ask4_price_ddx",
    "bid4_price_ddx",
    "ask4_vol_ddx",
    "ask5_price_ddx",
    "bid5_price_ddx",
    "ask5_vol_ddx",
    "ask6_price_ddx",
    "bid6_price_ddx",
    "ask6_vol_ddx",
    "ask7_price_ddx",
    "bid7_price_ddx",
    "ask7_vol_ddx",
    "ask8_price_ddx",
    "bid8_price_ddx",
    "ask8_vol_ddx",
    "ask9_price_ddx",
    "bid9_price_ddx",
    "ask9_vol_ddx",
    "ask10_price_ddx",
    "bid10_price_ddx",
    "ask10_vol_ddx",
]

config_file_path = "./config.json"

with open(config_file_path, "r") as handler:
    config = json.load(handler)

FEE = float(config["exchange"]["fee"])

host = config["database"]["host"]
port = int(config["database"]["port"])
user = config["database"]["user"]
password = config["database"]["password"]
database = config["database"]["database"]

tbar.update(10)

con = pymysql.connect(host, user=user, port=port, passwd=password, database=database)

tbar.update(20)

with con:
    # HAS TO BE ASCENDING ORDER
    query = "SELECT * FROM `kucoin`.`ethusdt` ORDER BY `record_time` ASC"
    df = pd.read_sql(query, con)

    # time-insensitive set

    # bid-ask spreads, mid-prices, and price differences (v2 and v3)
    for l in range(1, 11):
        # v2
        df[f"spread_{l}"] = df[f"ask{l}_price"] - df[f"bid{l}_price"]
        df[f"midprice_{l}"] = (df[f"ask{l}_price"] + df[f"bid{l}_price"]) / 2.0

        # v3
        if l > 1:
            df[f"ask_diff_{l}"] = df[f"ask{l}_price"] - df["ask1_price"]
            df[f"bid_diff_{l}"] = df["bid1_price"] - df[f"bid{l}_price"]
    tbar.update(20)

    # mean prices and volumes (v4)
    vols = [name for name in list(df.columns) if "_vol" in name]
    prices = [name for name in list(df.columns) if "_price" in name]
    ask_prices = [name for name in prices if "ask" in name]
    bid_prices = [name for name in prices if "bid" in name]
    ask_vols = [name for name in vols if "ask" in name]
    bid_vols = [name for name in vols if "bid" in name]

    df["avg_ask_price"] = df[ask_prices].mean(axis=1).round(6)
    df["avg_bid_price"] = df[bid_prices].mean(axis=1).round(6)
    df["avg_ask_vol"] = df[ask_vols].mean(axis=1).round(6)
    df["avg_bid_vol"] = df[bid_vols].mean(axis=1).round(6)
    tbar.update(10)

    # accumulated differences (v5)
    df["acc_price_diff"] = 0
    df["acc_vol_diff"] = 0
    for l in range(1, 11):
        df["acc_price_diff"] = (
            df["acc_price_diff"] + df[f"ask{l}_price"] - df[f"bid{l}_price"]
        ).round(6)
        df["acc_vol_diff"] = (
            df["acc_vol_diff"] + df[f"ask{l}_vol"] - df[f"bid{l}_vol"]
        ).round(6)

    tbar.update(20)

    # we are comparing the price this many minutes into the future to calculate the movement column
    time_span = int(sys.argv[1])

    # comparing midprice to the future midprice in {sys.argv[1]} rows
    df["movement"] = (
        (df["midprice_1"].shift(-int(sys.argv[1])) - df["midprice_1"])
        > ((df["midprice_1"] + df["midprice_1"].shift(-time_span)) * FEE)
    ) * 1  # converting a serie of bool to a serie of int

    # time-sensitive set

    # time difference
    df["time_diff"] = df["record_time"] - df["record_time"].shift(time_span)
    df["time_diff"] = df["time_diff"] / np.timedelta64(1, "s")

    # price and volume derivatives (v6)
    for l in range(1, 11):
        df[f"ask{l}_price_ddx"] = (
            (df[f"ask{l}_price"] - df[f"ask{l}_price"].shift(time_span))
            / (df["time_diff"] / 60.0)
        ).round(6)
        df[f"bid{l}_price_ddx"] = (
            (df[f"bid{l}_price"] - df[f"bid{l}_price"].shift(time_span))
            / (df["time_diff"] / 60.0)
        ).round(6)
        df[f"ask{l}_vol_ddx"] = (
            (df[f"ask{l}_vol"] - df[f"ask{l}_vol"].shift(time_span))
            / (df["time_diff"] / 60.0)
        ).round(6)
        df[f"ask{l}_vol_ddx"] = (
            (df[f"bid{l}_vol"] - df[f"bid{l}_vol"].shift(time_span))
            / (df["time_diff"] / 60.0)
        ).round(6)

    tbar.update(20)

    # calculating OBV
    # df["OBV"] = -1614347.8061
    # for i in range(1, len(df)):
    #     if df.loc[i, "midprice_1"] > df.loc[i - 1, "midprice_1"]:
    #         df.loc[i, "OBV"] = df.loc[i - 1, "OBV"] + df.loc[i, "vol"]
    #     elif df.loc[i, "midprice_1"] < df.loc[i - 1, "midprice_1"]:
    #         df.loc[i, "OBV"] = df.loc[i - 1, "OBV"] - df.loc[i, "vol"]
    #     else:
    #         df.loc[i, "OBV"] = df.loc[i - 1, "OBV"]

    df = df.drop(columns=["record_time", "time_diff"])
    tbar.update(5)

    # df = df.drop(columns=list(itertools.chain(v1, v2, v4)))
    tbar.update(5)

    df = df.dropna()
    tbar.update(5)

    # num of rows where 'movement' is 0
    num_movement_0 = len(df[df["movement"] == 0])
    # num of rows where 'movement' is 1
    num_movement_1 = len(df[df["movement"] == 1])

    shave_off = abs(
        num_movement_0 - num_movement_1
    )  # num of rows to drop so movement =0 and =1 are the same

    tbar.update(5)

    drop_list = []
    for index, row in df.iterrows():
        if shave_off == 0:
            break
        if row["movement"] == int(num_movement_0 < num_movement_1):
            drop_list.append(index)
            shave_off = shave_off - 1
    tbar.update(5)

    df = df.drop(drop_list)
    tbar.update(10)

    df.to_csv("kucoin_eth-usdt.csv", index=False)

    tbar.update(5)
    tbar.close()
    # fig, ax1 = plt.subplots()
    # color = "tab:red"
    # ax1.set_xlabel("time")
    # ax1.set_ylabel("price ($)")
    # ax1.plot(df["record_time"], df["midprice"], color=color)

    # ax2 = ax1.twinx()  # instantiate a second axes that shares the same
    # x-axis

    # color = "tab:blue"
    # ax2.set_ylabel("OBV", color=color)  # we already handled the x-label with ax1
    # ax2.plot(df["record_time"], df["OBV"], color=color)
    # ax2.tick_params(axis="y", labelcolor=color)

    # fig.tight_layout()  # otherwise the right y-label is slightly clipped
    # plt.show()
