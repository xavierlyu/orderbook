import pandas as pd
import pymysql
import json

config_file_path = "./config.json"

with open(config_file_path, "r") as handler:
    config = json.load(handler)

host = config["database"]["host"]
port = int(config["database"]["port"])
user = config["database"]["user"]
password = config["database"]["password"]
database = config["database"]["database"]

con = pymysql.connect(host, user=user, port=port, passwd=password, database=database)

with con:
    query = "SELECT * FROM `kucoin`.`ethusdt` ORDER BY `record_time` LIMIT 10"
    df = pd.read_sql(query, con)

    print(df)
