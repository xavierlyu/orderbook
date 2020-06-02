import pandas as pd
import numpy as np

import xgboost as xgb
from sklearn import metrics
import matplotlib.pyplot as plt

df = pd.read_csv(r'./kucoin_eth-usdt.csv')

Y = df['movement'].values

df = df.drop('movement', axis=1)
X = df.values

# Split dataset into training set and test set
l = int(len(X) * 0.95)
X_train = X[:l]
X_test = X[l:]
y_train = Y[:l]
y_test = Y[l:]

dtrain = xgb.DMatrix(X_train, y_train)
dtest = xgb.DMatrix(X_test, y_test)

watchlist = [(dtest, 'eval'), (dtrain, 'train')]
params = {'max-depth': 7, 'eta': 0.25, 'objective': 'binary:logistic'}
gbm = xgb.train(params, dtrain, 150, evals=watchlist)
preds = gbm.predict(xgb.DMatrix(X_test))

print(len(preds))
print(np.count_nonzero([1 if i > 0.5 else 0 for i in preds] == 1))

print("0.5 Accuracy:", metrics.accuracy_score(
    y_test, [1 if i > 0.5 else 0 for i in preds]))
print("0.6 Accuracy:", metrics.accuracy_score(
    y_test, [1 if i > 0.6 else 0 for i in preds]))
print("0.7 Accuracy:", metrics.accuracy_score(
    y_test, [1 if i > 0.7 else 0 for i in preds]))
print("0.8 Accuracy:", metrics.accuracy_score(
    y_test, [1 if i > 0.8 else 0 for i in preds]))
print("0.9 Accuracy:", metrics.accuracy_score(
    y_test, [1 if i > 0.9 else 0 for i in preds]))

xgb.plot_importance(gbm)
plt.show()
