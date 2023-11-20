# import library
from IPython.display import clear_output
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from math import sqrt
import warnings
warnings.filterwarnings('ignore')


# read data
WineQT_data = pd.read_csv(
    "D:\WorkTable\Artificial_Intelligence\Report02\WineQT.csv")
print(WineQT_data)

# cleaning data
# feature = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
# species = WineQT_data.dropna(subset=feature)
# data = WineQT_data[feature].copy()
# print(data)

# scale the data
data = ((WineQT_data - WineQT_data.min()) / (WineQT_data.max() - WineQT_data.min())) * \
    9 + 1    # (* 9 + 1): làm tròn dữ liệu và > 0
print(data)

# initialize random centroids


def randomCentroids(data, k):
    centroids = []
    for i in range(k):
        centroid = data.apply(lambda x: float(x.sample()))
        centroids.append(centroid)
    return pd.concat(centroids, axis=1)


centroids = randomCentroids(data=data, k=5)
# print(centroids)

# find label and clustering data


def getLabels(data, centroids):
    distances = centroids.apply(lambda x: np.sqrt(
        ((data - x) ** 2).sum(axis=1)))
    return distances.idxmin(axis=1)


labels = getLabels(data=data, centroids=centroids)
print('\n')
print(labels.value_counts())

# update the centroids


def newCentroids(data, labels, k):
    return data.groupby(labels).apply(lambda x: np.exp(np.log(x).mean())).T


print(newCentroids(data=data, labels=labels, k=3))

# plotting k_means iterations


def plotCluster(data, labels, centroids, iteration):
    pca = PCA(n_components=2)
    data_2d = pca.fit_transform(data)
    centroids_2d = pca.transform(centroids.T)
    clear_output(wait=True)
    plt.title(f'Iteration{iteration}')
    plt.scatter(x=data_2d[:, 0], y=data_2d[:, 1], c=labels)
    plt.scatter(x=centroids_2d[:, 0], y=centroids_2d[:, 1])
    plt.show()


max_iterations = 100
k = 2
centroids = randomCentroids(data=data, k=k)
old_centroids = pd.DataFrame()
iteration = 1

while (iteration < max_iterations) and not centroids.equals(old_centroids):
    old_centroids = centroids
    labels = getLabels(data=data, centroids=centroids)
    centroids = newCentroids(data=data, labels=labels, k=k)
    plotCluster(data=data, labels=labels,
                centroids=centroids, iteration=iteration)
    iteration += 1

# -----------------------------------------------------------------------------

