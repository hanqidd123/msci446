import numpy as np
import openpyxl
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

inputData = pd.read_csv("input_data.csv")

y = []
features = inputData.columns[:5639]
target = (inputData["Discipline"].values).reshape(len(inputData["Discipline"]), 1)
data = (inputData[features].values).reshape(len(inputData["Discipline"]), 5639)

print(target)
print(data)

mlNB = MultinomialNB()
mlNB.fit(data, target.ravel())
print(" *Coefficients: \n", mlNB.coef_)
print(" *Intercepts: \n", mlNB.intercept_)
predicted = mlNB.predict(data)

#MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
#print(mlNB.predict(X[2:3]))
print(" *Predictions: \n", mlNB.predict_proba(data))
print(" *Accuracy score for the model: \n", mlNB.score(data,target.ravel()))
