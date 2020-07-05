# Predicting Mid Price Movement w/ Order Book Data

A python implemention of [Kercheval, Alec & Zhang, Yuan. (2015). Modelling high-frequency limit order book dynamics with support vector machines. Quantitative Finance. 15. 1-15. 10.1080/14697688.2015.1032546.](https://www.math.fsu.edu/~aluffi/archive/paper462.pdf)

## Collecting Data

Every 60 seconds, `collect_data.py` would collect the limit order book data from level 1 to level 10 from [Kucoin ETH-USDT](https://www.kucoin.com/trade) through a HTTP GET request and store it as an entry in AWS RDS. We did not provide the endpoint, password, etc. to our database for obvious reasons. We hosted the script on EC2 for it to collect data nonstop. 

## Features and Labelling Data

In addition to the features proposed by the research paper, we added two more features: market depths and imbalance. 





