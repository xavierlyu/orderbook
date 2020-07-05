import pymysql
import requests
import time
from datetime import datetime
import json
import pytz

config_file_path = "./config.json"

with open(config_file_path, "r") as handler:
    config = json.load(handler)

host = config["database"]["host"]
port = int(config["database"]["port"])
user = config["database"]["user"]
password = config["database"]["password"]
database = config["database"]["database"]

connection = pymysql.connect(
    host, user=user, port=port, passwd=password, database=database
)

while 1:
    try:
        r = requests.get(
            "https://api.kucoin.com/api/v1/market/orderbook/level2_100?symbol=ETH-USDT"
        )

        curr_timestamp = str(datetime.now(pytz.utc))[:-6]
        data = r.json()
        orderbook_data = data["data"]
        arr = []
        for i in range(10):
            arr.append(orderbook_data["asks"][i][0])
            arr.append(orderbook_data["asks"][i][1])
            arr.append(orderbook_data["bids"][i][0])
            arr.append(orderbook_data["bids"][i][1])

        # record-time
        arr.append(curr_timestamp)

        print(
            (float(orderbook_data["asks"][0][0]) + float(orderbook_data["bids"][0][0]))
            / 2.0
        )

        with connection.cursor() as cursor:
            sql = "INSERT INTO `ethusdt` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(arr))

        connection.commit()
        time.sleep(60)

    except:
        time.sleep(30)


"""
for i in range(50):
    print('ask' + str(i) + '_price float(10) NULL,')
    print('ask' + str(i) + '_vol float(10) NULL,')
    print('bid' + str(i) + '_price float(10) NULL,')
    print('bid' + str(i) + '_vol float(10) NULL,')
"""
