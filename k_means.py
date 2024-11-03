import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def kmeans(data, k, max_iters=100):
   
    centroids = data.sample(n=k).to_numpy()  

    for _ in range(max_iters):
       
        distances = np.linalg.norm(data.values[:, np.newaxis] - centroids, axis=2)  
        closest_centroids = np.argmin(distances, axis=1)  
        
        
        new_centroids = np.array([data.values[closest_centroids == i].mean(axis=0) for i in range(k)])
        
        
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids  

    return closest_centroids, centroids


def main():
    
    num_points = int(input("Enter the number of data points: "))
    

    data_points = [
        list(map(float, input("Enter a data point in the format 'x,y': ").split(','))) 
        for _ in range(num_points)
    ]
    
  
    data = pd.DataFrame(data_points, columns=['Feature1', 'Feature2'])

   
    num_clusters = int(input("Enter the number of clusters: "))

   
    cluster_labels, centroids = kmeans(data, num_clusters)

  
    data['Cluster'] = cluster_labels

    
    plt.figure(figsize=(8, 6))
    for i in range(num_clusters):
        plt.scatter(data[data['Cluster'] == i]['Feature1'], data[data['Cluster'] == i]['Feature2'], label=f'Cluster {i+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='X', s=200, label='Centroids')  # Plot centroids
    plt.title('K-means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
