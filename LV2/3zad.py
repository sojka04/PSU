import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()

img_posvijetljena = np.clip(img * 1.5, 0, 255)  

img_rotirana = np.rot90(img, -1) 

img_zrcaljena = np.fliplr(img)

img_smanjena = img[::10, ::10]  

img_cetvrtina = np.zeros_like(img)  
width = img.shape[1] // 4  
img_cetvrtina[:, width:2*width] = img[:, width:2*width]

plt.figure(figsize=(10, 8))

plt.subplot(2, 3, 1)
plt.imshow(img_posvijetljena, cmap="gray")
plt.title("Posvijetljena slika")
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img_rotirana, cmap="gray")
plt.title("Rotirana slika")
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(img_zrcaljena, cmap="gray")
plt.title("Zrcaljena slika")
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(img_smanjena, cmap="gray")
plt.title("Smanjena rezolucija")
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(img_cetvrtina, cmap="gray")
plt.title("Druga četvrtina")
plt.axis('off')

plt.show()
