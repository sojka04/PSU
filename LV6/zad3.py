from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

def generate_data(n, f):
    if f == 1:
        X, _ = datasets.make_blobs(n_samples=n, random_state=365)
    elif f == 2:
        X, _ = datasets.make_blobs(n_samples=n, random_state=148)
        X = np.dot(X, [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]])
    elif f == 3:
        X, _ = datasets.make_blobs(n_samples=n, centers=4, cluster_std=[1.0, 2.5, 0.5, 3.0], random_state=148)
    elif f == 4:
        X, _ = datasets.make_circles(n_samples=n, factor=0.5, noise=0.05)
    elif f == 5:
        X, _ = datasets.make_moons(n_samples=n, noise=0.05)
    else:
        X = []
    return X

X = generate_data(25, 5)
Z = linkage(X, method="ward")

plt.figure(figsize=(10, 7))
dendrogram(Z, labels=[f"Podatak {i+1}" for i in range(len(X))])
plt.ylabel('Udaljenost')
plt.show()
