import itertools
import SVM
import pandas as pd
import csv
import time
import json

if __name__ == "__main__":
    constants_file_path = "./constants.json"
    output_csv_file_path = "./trials_levels.csv"

    with open(constants_file_path, "r") as handler:
        constants = json.load(handler)

    v1 = constants["v1"]
    v2 = constants["v2"]
    v3 = constants["v3"]
    v4 = constants["v4"]
    v5 = constants["v5"]
    v6 = constants["v6"]
    v7 = constants["v7"]
    v8 = constants["v8"]

    all_features = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8

    level2_features = list(filter(lambda x: "2" in x, all_features))
    level3_features = list(filter(lambda x: "3" in x, all_features))
    level4_features = list(filter(lambda x: "4" in x, all_features))
    level5_features = list(filter(lambda x: "5" in x, all_features))
    level6_features = list(filter(lambda x: "6" in x, all_features))
    level7_features = list(filter(lambda x: "7" in x, all_features))
    level8_features = list(filter(lambda x: "8" in x, all_features))
    level9_features = list(filter(lambda x: "9" in x, all_features))
    level10_features = list(filter(lambda x: "10" in x, all_features))
    level1_features = [
        item
        for item in list(filter(lambda x: "1" in x, all_features))
        if item not in level10_features
    ]

    with open(output_csv_file_path, "a") as csvFile:
        row = [
            "Name",
            "Accuracy",
            "Precision",
            "Recall",
            "Filename",
            "Time Taken",
        ]
        writer = csv.writer(csvFile)
        writer.writerow(row)

    start_time = time.time()
    df = pd.read_csv(r"./kucoin_eth-usdt.csv")
    output_name = "level1-5_2"
    df = df.drop(
        columns=(
            level1_features
            + level2_features
            + level3_features
            + level4_features
            + level5_features
        )
    )
    a, p, r, yp, yt, fn = SVM.main2(df, output_name)
    with open(output_csv_file_path, "a") as csvFile:
        row = [output_name, a, p, r, fn, str(time.time() - start_time)]
        writer = csv.writer(csvFile)
        writer.writerow(row)

    start_time = time.time()
    df = pd.read_csv(r"./kucoin_eth-usdt.csv")
    output_name = "level1-3_2"
    df = df.drop(columns=(level1_features + level2_features + level3_features))
    a, p, r, yp, yt, fn = SVM.main2(df, output_name)
    with open(output_csv_file_path, "a") as csvFile:
        row = [output_name, a, p, r, fn, str(time.time() - start_time)]
        writer = csv.writer(csvFile)
        writer.writerow(row)
