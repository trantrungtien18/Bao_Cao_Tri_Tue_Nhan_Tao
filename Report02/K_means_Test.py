import matplotlib as plt
from sklearn.cluster import KMeans
import numpy as nb
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


data = pd.read_csv("D:/WorkTable/Artificial_Intelligence/Report02/IRIS.csv")
print(data)

kmeans = KMeans(n_clusters=2, random_state=0)
data['cluster'] = kmeans.fit_predict(
    data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
print(data)

meanOfCluster = kmeans.cluster_centers_
print(meanOfCluster)
# cen_sepal_length = []
# print(center_x)
# print(center_y)
