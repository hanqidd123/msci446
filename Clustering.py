from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
import openpyxl
import numpy as np

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

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02  # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
                   extent=(xx.min(), xx.max(), yy.min(), yy.max()),
                   cmap=plt.cm.Paired,
                   aspect='auto', origin='lower')

plt.plot(x[:, 0], x[:, 1], 'k.', markersize=2)
 # Plot the centroids as a white X
centroids = model.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
        marker='x', s=169, linewidths=3,
        color='w', zorder=10)
plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
                  'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()