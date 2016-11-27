from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
import openpyxl
import numpy as np

wb = openpyxl.load_workbook('clean_data_test.xlsx')
dataStr = wb.get_sheet_by_name("data")
documents = ["human machine interface for la babc computer applications",
             "a survey of user opinion of computer system respose time","the eps user interface management system",
             "relation of user perceived response time to error measurement",
             "the generation of random binary unordered trees",
             "the intersection graph of paths in trees",
             "graph minors IV widths of trees and well quasi ordering",
             "graph minors a survey"]


true_k = 8
vectorizer = TfidfVectorizer(stop_words="english")
x = vectorizer.fit_transform(documents)
print(x)
model = KMeans(n_clusters=true_k, init="k-means++", max_iter=100, n_init=1)
model.fit(x)

order_centroids = model.cluster_centers_.argsort()[:,::-1]
terms = vectorizer.get_feature_names()
total_inertia = 0
for i in range(true_k):
    print(" ")
    print("Cluster" + str(i))
    print("Sum of distances of samples to their closest cluster center: ", model.inertia_)
    total_inertia = total_inertia + model.inertia_
    for ind in order_centroids[i, :10]:
        print(terms[ind])

    #average = total_inertia / true_k
    #print("Average Inertia for ", true_k, "clusters is" , average)