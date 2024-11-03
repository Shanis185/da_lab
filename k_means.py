import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




def main():
    num_points=int(input("enter the number of data points"))
    data_points=[]
    print("enter the datapoints in format x,y ")
    for i in range(num_points):
        points=input()
        x,y=map(float,points.split(","))
        data_points.append([x,y])

        data=pd.DataFrame(data_points,columns=['feature 1','feature 2'])
        num_clusters=int(input("enter the number of clusters"))

        cluster_label,centroids=kmeans(data,num_clusters)

        data['cluster']=cluster_label

