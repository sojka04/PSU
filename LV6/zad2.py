from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

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

X = generate_data(500, 5)
inertia = []

for k in range(2, 21):
	model = KMeans(n_clusters=k, random_state=0)
	model.fit(X)
	inertia.append(model.inertia_)

plt.plot(range(2, 21), inertia, marker='o')
plt.xlabel('Broj klastera')
plt.ylabel('Kriterijska vrijednost')
plt.title('Kriterijska funkcija za KMeans')
plt.grid()
plt.show()
