#import libraries
import csv
import Orange
import numpy as np
from numpy import linalg as LA
from sklearn.cluster import KMeans

#The dirctory should be modified
csvFile = Orange.data.Table("/Users/Oliver/Desktop/香港大學研究生/Data Mining/Assignment1/stock_data.csv")
X = csvFile

#Normalization function 
def normalize(data): 
	data = data / np.linalg.norm(data,ord = 2)
	return data 

#Stock Name acquired
stockName = [0 for col in range(30)]
for i in range(30):
	stockName[i] = X[i][-1]

#Call normliazation function 
'''
for i in range(30):
	X[i] = normalize(X[i])
'''

#Kmeans algorithm
n_cluster = 8 # modfied for number of clusters
kmeans = KMeans(init='random', n_clusters=n_cluster, max_iter=10000, n_init=5).fit(X)
print(kmeans.labels_) #labels
print(kmeans.inertia_) #SSE

#lables assignmenta and Output
for n in range(n_cluster):
    output = []
    for i in range(30):
        if kmeans.labels_[i] == n:
            output.append(stockName[i])
    print("label ",n + 1," contains ")
    print(output)