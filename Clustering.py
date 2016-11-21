from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import openpyxl

wb = openpyxl.load_workbook('clean_data_test.xlsx')
dataStr = wb.get_sheet_by_name("data")
documents = []

for i in range(1,4476):
    print(i)
    print(dataStr.cell(row=3, column=i).value)
    documents.append(dataStr.cell(row=3, column=i).value)

true_k = 5
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(documents)
print(x)
model = KMeans(n_clusters=true_k, init="k-means++", max_iter=100, n_init=1)

model.fit(x)
order_centroids = model.cluster_centers_.argsort()[:,::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print(" ")
    print("Cluster" + str(i))
    for ind in order_centroids[i, :10]:
        print(terms[ind])