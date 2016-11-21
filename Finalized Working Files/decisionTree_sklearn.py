from __future__ import print_function
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
from sklearn.cross_validation import KFold, cross_val_score
from sklearn import preprocessing
import os
import subprocess
import pandas as pd
import numpy as np

inputData = pd.read_csv("DT_input.csv", index_col=0)

#print("* inputData.head()", inputData.head(), end="\n\n")
#print("* inputData.tail()", inputData.tail(), end="\n\n")
#print("* Unique Discipline:", inputData["Discipline"].unique())

features = list(inputData.columns[:5639])
class_name = list(inputData["Discipline"].unique())
# data = (inputData.ix[:5639].values).reshape((len(inputData["Discipline"]), 89))

print("* features:", features)
print("* targets:", class_name)

target = inputData["Discipline"]
data = inputData[features]

# min_samples_split = number of samples in a node for it to be split
# dt = DecisionTreeClassifier(min_samples_split=10, random_state=90)
dt = DecisionTreeClassifier(criterion="entropy")
dt.fit(data, target)

with open("dt.dot", 'w') as f:
    f = tree.export_graphviz(dt, out_file=f, feature_names=features, class_names=class_name, filled=True)

predicted = dt.predict(data)
print("* Predictions: \n", np.array([predicted]).T)
print("* Probability of prediction: \n", dt.predict_proba(data))
print("* Feature importance: ", dt.feature_importances_)
print("* Accuracy score for the model: \n", dt.score(data, target))
print(metrics.confusion_matrix(target, predicted, labels=class_name))

model = DecisionTreeClassifier(criterion="entropy")
kf = KFold(len(target), n_folds=5)
scores = cross_val_score(estimator=model, X=data, y=target, cv=kf, scoring='accuracy')
print("MSE of every fold in 10 fold cross validation: ", abs(scores))
print("Mean of the 10 fold cross-validation: %0.2f" % abs(scores.mean()))

# graph of the decision tree
def visualize_tree(tree, feature_names):
    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f, feature_names=feature_names)
    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to produce visualization.")
visualize_tree(dt, features)
