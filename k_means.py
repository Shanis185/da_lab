import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def kmeans(data,k,max_iters=100):
    centroids=np.sample(n=k).to_numpy
    for _ in range (max_iters):
        distance=np.linalg.norm(data.values[:,np.newaxis]-centroids,axis=2)
        closest_centroids=np.argmin(distance,axis=1)


        new_centroids=np.array([data.values[closest_centroids==i].mean(axis=0) for i in range(k)])

        if np.all(centroids=new_centroids):
            break
        centroids=new_centroids

    return closest_centroids,centroids

        




def main():
    num_points=int(input("enter the number of data points"))
    data_points=[]
    print("enter the datapoints in format x,y ")
    for _ in range(num_points):
        points=input()
        x,y=map(float,points.split(","))
        data_points.append([x,y])

        data=pd.DataFrame(data_points,columns=['feature 1','feature 2'])
        num_clusters=int(input("enter the number of clusters"))

        cluster_label,centroids=kmeans(data,num_clusters)

        data['cluster']=cluster_label

