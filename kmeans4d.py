import numpy as np
class KMeansClustering:
    def __init__(self, X, num_clusters):
        self.K = num_clusters # cluster number
        self.max_iterations = 100 # max iteration. don't want to run inf time
        self.num_examples, self.num_features = X.shape # num of examples, num of features
        

    # randomly initialize centroids
    def initialize_random_centroids(self, X):
        centroids = np.zeros((self.K, self.num_features)) # row , column full with zero
        for k in range(self.K): 
            centroid = X[np.random.choice(range(self.num_examples))] 
            centroids[k] = centroid
        return centroids
    # create cluster Function
    def create_cluster(self, X, centroids):
        clusters = [[] for i in range(self.K)]
        for point_idx, point in enumerate(X):
            closest_centroid = np.argmin(np.sqrt(np.sum((point-centroids)**2, axis=1)))
            clusters[closest_centroid].append(point_idx)
        return clusters 
    
    # new centroids
    def calculate_new_centroids(self, clusters, X):
        centroids = np.zeros((self.K, self.num_features)) # row , column full with zero
        for idx, cluster in enumerate(clusters):
            new_centroid = np.mean(X[cluster], axis=0) # find the value for new centroids
            centroids[idx] = new_centroid
        return centroids
    
        
    # fit data
    def fit(self, X):
        centroids = self.initialize_random_centroids(X) # initialize random centroids
        for _ in range(self.max_iterations):
            clusters = self.create_cluster(X, centroids) # create cluster
            previous_centroids = centroids
            centroids = self.calculate_new_centroids(clusters, X) # calculate new centroids
            diff = centroids - previous_centroids # calculate difference
            if not diff.any():
                break
        return centroids,clusters

class Kmeans4d():
    def __init__(self):
        with open("train4dAll.txt","r") as f:
            Data=f.read().splitlines()
        self.data=Data
        self.X=np.zeros((len(Data),3))
        self.truth=np.zeros(len(Data))
        self.load_data()

    def load_data(self):
        idx=-1
        for ds in self.data:
            idx+=1
            ds=ds.split(" ")
            self.truth[idx]=float(ds[3])
            ds=ds[:-1]
            for d_idx, d in enumerate(ds):
                self.X[idx][d_idx]=float(d)
    def start_cluster(self):
        np.random.seed(10)
        num_clusters = 10 # num of cluster
        kmeans_result = KMeansClustering(self.X, num_clusters)
        Centers,Clusters = kmeans_result.fit(self.X)
        return Centers,Clusters,kmeans_result