import json
import time
import base64
import hmac
import hashlib
import requests
import pymysql


class Order_Executor:
    def __init__(self, is_sandbox=True):
        config_file_path = "./config.json"

        with open(config_file_path, "r") as handler:
            self.config = json.load(handler)

        if is_sandbox:
            self.api_key = self.config["sandbox_api"]["key"]
            self.api_secret = self.config["sandbox_api"]["secret"]
            self.api_passphrase = self.config["sandbox_api"]["passphrase"]
        else:
            self.api_key = self.config["api"]["key"]
            self.api_secret = self.config["api"]["secret"]
            self.api_passphrase = self.config["api"]["passphrase"]

        self.base_url = (
            "https://openapi-sandbox.kucoin.com"
            if is_sandbox
            else "https://api.kucoin.com"
        )

    def place_market_order(self, side, funds):
        api_endpoint = "/api/v1/orders"

        url = f"{self.base_url}{api_endpoint}"
        now = int(time.time() * 1000)
        data = {
            "clientOid": str(now),
            "side": side,
            "symbol": "ETH-USDT",
            "type": "market",
            "funds": funds,
        }
        data_json = json.dumps(data)
        str_to_sign = str(now) + "POST" + api_endpoint + data_json
        signature = self._sign(str_to_sign)

        headers = {
            "Content-Type": "application/json",
            "KC-API-KEY": self.api_key,
            "KC-API-SIGN": signature,
            "KC-API-TIMESTAMP": str(now),
            "KC-API-PASSPHRASE": self.api_passphrase,
        }
        response = requests.request("POST", url, headers=headers, data=data_json)
        print(response.status_code)
        print(response.json())

        self._store_order_id(
            now, response.json()["data"]["orderId"], "sandbox" in self.base_url
        )

        return response.json

    def list_orders(self):
        api_endpoint = "/api/v1/hist-orders"

        url = f"{self.base_url}{api_endpoint}"
        now = int(time.time() * 1000)
        str_to_sign = str(now) + "GET" + api_endpoint
        signature = self._sign(str_to_sign)

        headers = {
            "Content-Type": "application/json",
            "KC-API-KEY": self.api_key,
            "KC-API-SIGN": signature,
            "KC-API-TIMESTAMP": str(now),
            "KC-API-PASSPHRASE": self.api_passphrase,
        }
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        print(response.json())

        return response.json

    def get_order(self, orderId):
        api_endpoint = f"/api/v1/orders/{orderId}"

        url = f"{self.base_url}{api_endpoint}"
        now = int(time.time() * 1000)
        str_to_sign = str(now) + "GET" + api_endpoint
        signature = self._sign(str_to_sign)

        headers = {
            "Content-Type": "application/json",
            "KC-API-KEY": self.api_key,
            "KC-API-SIGN": signature,
            "KC-API-TIMESTAMP": str(now),
            "KC-API-PASSPHRASE": self.api_passphrase,
        }
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        print(response.json())

        return response.json

    def _sign(self, str_to_sign):
        return base64.b64encode(
            hmac.new(
                self.api_secret.encode("utf-8"),
                str_to_sign.encode("utf-8"),
                hashlib.sha256,
            ).digest()
        )

    def _store_order_id(self, timestamp, order_id, is_sandbox):
        host = self.config["database"]["host"]
        port = int(self.config["database"]["port"])
        user = self.config["database"]["user"]
        password = self.config["database"]["password"]
        database = self.config["database"]["database"]

        connection = pymysql.connect(
            host, user=user, port=port, passwd=password, database=database
        )

        with connection.cursor() as cursor:
            arr = [str(timestamp), order_id, is_sandbox]
            sql = "INSERT INTO `orders` VALUES (%s, %s, %s)"
            cursor.execute(sql, tuple(arr))

        connection.commit()


test_order_placer = Order_Executor()

# test_order_placer.place_market_order(5)
# test_order_placer.get_order("5edb03b01794c300063a1541")
