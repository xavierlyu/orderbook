import itertools
import SVM
import pandas as pd
import csv
import time

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

# return accuracy, precision, recall, list(y_pred), list(y_test), filename (SVM.main2(df,fn))

with open("Trials.csv", "a") as csvFile:
    row = [
        "V1",
        "V2",
        "V3",
        "V4",
        "V5",
        "V6",
        "Accuracy",
        "Prediction",
        "Recall",
        "Y_Pred",
        "Y_Test",
        "Filename",
        "Time Taken",
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# #Singular Cases

# #Case V1
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v2, v3, v4, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["Y", "N", "N", "N", "N", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V2
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v1, v3, v4, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["N", "Y", "N", "N", "N", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V3
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v1, v2, v4, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v3")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["N", "N", "Y", "N", "N", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V4
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v1, v2, v3, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v4")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["N", "N", "N", "Y", "N", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V5
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v1, v2, v3, v4, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v5")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["N", "N", "N", "N", "Y", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V6
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v1, v2, v3, v4, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v6")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["N", "N", "N", "N", "N", "Y", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Double Cases V1

# #Case V1V2
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v3, v4, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v2")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["Y", "Y", "N", "N", "N", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V1V3
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v2, v4, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v3")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["Y", "N", "Y", "N", "N", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V1V4
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v2, v3, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v4")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["Y", "N", "N", "Y", "N", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V1V5
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v2, v3, v4, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v5")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["Y", "N", "N", "N", "Y", "N", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# #Case V1V6
# start_time = time.time()
# df = pd.read_csv(r'./kucoin_eth-usdt.csv')
# df = df.drop(columns=list(itertools.chain(v2, v3, v4, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v6")
# with open('Trials.csv', 'a') as csvFile:
# 	row = ["Y", "N", "N", "N", "N", "Y", a, p, r, yp, yt, fn, str(time.time() - start_time)]
# 	writer = csv.writer(csvFile)
# 	writer.writerow(row)

# # Double Cases V2

# # Case V2V3
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v4, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v3")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "Y",
#         "N",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V2V4
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v3, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v4")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "N",
#         "Y",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V2V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v3, v4, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "N",
#         "N",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V2V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v3, v4, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "N",
#         "N",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V3

# # Case V3V4
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v3v4")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "Y",
#         "Y",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V3V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v4, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v3v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "Y",
#         "N",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V3V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v4, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v3v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "Y",
#         "N",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V4

# # Case V4V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v3, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v4v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "N",
#         "Y",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V4V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v3, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v4v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "N",
#         "Y",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V5

# # Case V5V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v3, v4)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v5v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "N",
#         "N",
#         "Y",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Triple Cases V1

# # Double Cases V2

# # Case V1V2V3
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v4, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "Y",
#         "Y",
#         "N",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V1V2V4
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v3, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v4")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "Y",
#         "N",
#         "Y",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V1V2V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v3, v4, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "Y",
#         "N",
#         "N",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V1V2V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v3, v4, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "Y",
#         "N",
#         "N",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V3

# # Case V1V3V4
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v2, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v3v4")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "N",
#         "Y",
#         "Y",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V1V3V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v2, v4, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v3v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "N",
#         "Y",
#         "N",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V1V3V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v2, v4, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v3v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "N",
#         "Y",
#         "N",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# Double Cases V4

# Case V1V4V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v2, v3, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v4v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "N",
#         "N",
#         "Y",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V1V4V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v2, v3, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v4v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "N",
#         "N",
#         "Y",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V5

# # Case V1V5V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v2, v3, v4)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v5v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "N",
#         "N",
#         "N",
#         "Y",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Triple Cases V2

# # Double Cases V3

# # Case V2V3V4
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v3v4")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "Y",
#         "Y",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V2V3V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v4, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v3v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "Y",
#         "N",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V2V3V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v4, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v3v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "Y",
#         "N",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V4

# # Case V2V4V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v3, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v4v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "N",
#         "Y",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V2V4V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v3, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v4v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "N",
#         "Y",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V5

# # Case V2V5V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v3, v4)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v2v5v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "Y",
#         "N",
#         "N",
#         "Y",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Triple Cases V3

# # Double Cases V4

# # Case V3V4V5
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v3v4v5")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "Y",
#         "Y",
#         "Y",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Case V3V4V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v5)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v3v4v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "Y",
#         "Y",
#         "N",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Double Cases V5

# # Case V3V5V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v4)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v3v5v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "Y",
#         "N",
#         "Y",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Triple Cases V4

# # Double Cases V5

# # Case V4V5V6
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v1, v2, v3)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v4v5v6")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "N",
#         "N",
#         "N",
#         "Y",
#         "Y",
#         "Y",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# # Quadruple Cases V1

# # Triple Cases V2

# # Double Cases V3

# # Case V1V2V3V4
# start_time = time.time()
# df = pd.read_csv(r"./kucoin_eth-usdt.csv")
# df = df.drop(columns=list(itertools.chain(v5, v6)))
# a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3v4")
# with open("Trials.csv", "a") as csvFile:
#     row = [
#         "Y",
#         "Y",
#         "Y",
#         "Y",
#         "N",
#         "N",
#         a,
#         p,
#         r,
#         yp,
#         yt,
#         fn,
#         str(time.time() - start_time),
#     ]
#     writer = csv.writer(csvFile)
#     writer.writerow(row)

# Case V1V2V3V5
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v4, v6)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3v5")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
        "N",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Case V1V2V3V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v4, v5)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "Y",
        "N",
        "N",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Double Cases V4

# Case V1V2V4V5
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v3, v6)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v4v5")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "N",
        "Y",
        "Y",
        "N",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Case V1V2V4V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v3, v5)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v4v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "N",
        "Y",
        "N",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Double Cases V5

# Case V1V2V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v3, v4)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "N",
        "N",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Triple Cases V3

# Double Cases V4

# Case V1V3V4V5
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v2, v6)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v3v4v5")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "N",
        "Y",
        "Y",
        "Y",
        "N",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Case V1V3V4V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v2, v5)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v3v4v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "N",
        "Y",
        "Y",
        "N",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Double Cases V5

# Case V1V3V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v2, v4)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v3v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "N",
        "Y",
        "N",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Triple Cases V4

# Double Cases V5

# Case V1V4V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v2, v3)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v4v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "N",
        "N",
        "Y",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Quadruple Cases V2

# Triple Cases V3

# Double Cases V4

# Case V2V3V4V5
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v1, v6)))
a, p, r, yp, yt, fn = SVM.main2(df, "v2v3v4v5")
with open("Trials.csv", "a") as csvFile:
    row = [
        "N",
        "Y",
        "Y",
        "Y",
        "Y",
        "N",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Case V2V3V4V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v1, v5)))
a, p, r, yp, yt, fn = SVM.main2(df, "v2v3v4v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "N",
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Double Cases V5

# Case V2V3V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v1, v4)))
a, p, r, yp, yt, fn = SVM.main2(df, "v2v3v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "N",
        "Y",
        "Y",
        "N",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Triple Cases V4

# Double Cases V5

# Case V2V4V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v1, v3)))
a, p, r, yp, yt, fn = SVM.main2(df, "v2v4v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "N",
        "Y",
        "N",
        "Y",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Quadruple Cases V3

# Triple Cases V4

# Double Cases V5

# Case V3V4V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v1, v2)))
a, p, r, yp, yt, fn = SVM.main2(df, "v3v4v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "N",
        "N",
        "Y",
        "Y",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Quintuple Cases V1

# Quadruple Cases V2

# Triple Cases V3

# Double Cases V4

# Case V1V2V3V4V5
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v6)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3v4v5")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
        "N",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Case V1V2V3V4V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v5)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3v4v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Double Cases V5

# Case V1V2V3V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v4)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "Y",
        "N",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Triple Cases V4

# Double Cases V5

# Case V1V2V4V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v3)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v4v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "N",
        "Y",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Quadruple Cases V3

# Triple Cases V4

# Double Cases V5

# Case V1V3V4V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v2)))
a, p, r, yp, yt, fn = SVM.main2(df, "v1v3v4v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "N",
        "Y",
        "Y",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Quintuple Cases V2

# Quadruple Cases V3

# Triple Cases V4

# Double Cases V5

# Case V2V3V4V5V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
df = df.drop(columns=list(itertools.chain(v1)))
a, p, r, yp, yt, fn = SVM.main2(df, "v2v3v4v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "N",
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)

# Final Case V1-V6
start_time = time.time()
df = pd.read_csv(r"./kucoin_eth-usdt.csv")
a, p, r, yp, yt, fn = SVM.main2(df, "v1v2v3v4v5v6")
with open("Trials.csv", "a") as csvFile:
    row = [
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
        "Y",
        a,
        p,
        r,
        yp,
        yt,
        fn,
        str(time.time() - start_time),
    ]
    writer = csv.writer(csvFile)
    writer.writerow(row)
