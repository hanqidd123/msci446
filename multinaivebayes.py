import numpy as np
import openpyxl
import pandas as pd


inputData = pd.read_csv("input_data.csv")
print(inputData)
y = []
features = inputData.columns[:5639]
target = (inputData["Discipline"].values).reshape(len(inputData["Discipline"]), 1)
data = (inputData[features].values).reshape(len(inputData["Discipline"]), 5639)

X = data
y.append(target)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print(clf.predict(X[2:3]))
