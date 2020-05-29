import numpy as np
import cvxopt
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from tqdm import tqdm


class SVM:
    def fit(self, X, y):
        n_samples, n_features = X.shape
# P = X^T X
        K = np.zeros((n_samples, n_samples))
        for i in tqdm(range(n_samples)):
            for j in tqdm(range(n_samples)):
                K[i,j] = np.dot(X[i], X[j])
        P = cvxopt.matrix(np.outer(y, y) * K)
# q = -1 (1xN)
        q = cvxopt.matrix(np.ones(n_samples) * -1)
# A = y^T 
        A = cvxopt.matrix(y, (1, n_samples))
# b = 0 
        b = cvxopt.matrix(0.0)
# -1 (NxN)
        G = cvxopt.matrix(np.diag(np.ones(n_samples) * -1))
# 0 (1xN)
        h = cvxopt.matrix(np.zeros(n_samples))
        
        #line below doesn't work, use main2 for now. 
        solution = cvxopt.solvers.qp(P, q, G, h, A, b)
        
# Lagrange multipliers
        a = np.ravel(solution['x'])
# Lagrange have non zero lagrange multipliers
        sv = a > 1e-5
        ind = np.arange(len(a))[sv]
        self.a = a[sv]
        self.sv = X[sv]
        self.sv_y = y[sv]
# Intercept
        self.b = 0
        for n in range(len(self.a)):
            self.b += self.sv_y[n]
            self.b -= np.sum(self.a * self.sv_y * K[ind[n], sv])
        self.b /= len(self.a)
# Weights
        self.w = np.zeros(n_features)
        for n in range(len(self.a)):
            self.w += self.a[n] * self.sv_y[n] * self.sv[n]
        
    def project(self, X):
        return np.dot(X, self.w) + self.b
    
    
    def predict(self, X):
        return np.sign(self.project(X))

def main1():
        df = pd.read_csv(r'./kucoin_eth-usdt.csv')
        
        Y = df['movement'].values[:100]
        df = df.drop('movement', axis=1)
        X = df.values[:100]
        
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.33, random_state=42)
        
        svm = SVM()
        svm.fit(X_train, y_train)
        
        svc = LinearSVC()
        svc.fit(X_train, y_train)
        
        plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='winter');
        
        ax = plt.gca()
        xlim = ax.get_xlim()
        w = svc.coef_[0]
        a = -w[0] / w[1]
        xx = np.linspace(xlim[0], xlim[1])
        yy = a * xx - svc.intercept_[0] / w[1]
        plt.plot(xx, yy)
        yy = a * xx - (svc.intercept_[0] - 1) / w[1]
        plt.plot(xx, yy, 'k--')
        yy = a * xx - (svc.intercept_[0] + 1) / w[1]
        plt.plot(xx, yy, 'k--')
        
        y_pred = svc.predict(X_test)
        confusion_matrix(y_test, y_pred)
        
from sklearn import svm
from sklearn import metrics

def main2():
        #Create a svm Classifier
        clf = svm.SVC(kernel='linear', verbose = True) # Linear Kernel

        df = pd.read_csv(r'./kucoin_eth-usdt.csv')
        
        Y = df['movement'].values #[:100]
        df = df.drop('movement', axis=1)
        X = df.values #[:100]
        
        print(X)
        print(Y)
        
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.33, random_state=42)
        print("Train Test Split Complete")

        #Train the model using the training sets
        clf.fit(X_train, y_train)
        print("Fitting Complete")

        #Predict the response for test dataset
        y_pred = clf.predict(X_test)
        print("Prediction Complete")
        
        print(list(y_pred))
        print(list(y_test))
        [print(a, b) for a, b in zip(y_pred, y_test) if a!=b]

        
        print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

        # Model Precision: what percentage of positive tuples are labeled as such?
        print("Precision:",metrics.precision_score(y_test, y_pred))

        # Model Recall: what percentage of positive tuples are labelled as such?
        print("Recall:",metrics.recall_score(y_test, y_pred))
        
# print("\nMain 1 Running: \n")
# main1()

print("\nMain 2 Running: \n")
main2()