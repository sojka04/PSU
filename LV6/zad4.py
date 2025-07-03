from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('example_grayscale.png')
if len(img.shape) == 3:
    img = np.mean(img, axis=2)

X = img.reshape((-1, 1))
n_clusters = 10

model = KMeans(n_clusters=n_clusters, n_init=10)
model.fit(X)
centers = model.cluster_centers_.squeeze()
labels = model.labels_

img_compressed = np.choose(labels, centers)
img_compressed.shape = img.shape

plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Originalna slika')

plt.figure()
plt.imshow(img_compressed, cmap='gray')
plt.title(f'Kvantizacija sa {n_clusters} klastera')
plt.show()

original_bits = 8
compressed_bits = int(np.ceil(np.log2(n_clusters)))
compression_ratio = (compressed_bits / original_bits) * 100
print(f'Kompresija: {compression_ratio:.2f}% originalne veličine')
