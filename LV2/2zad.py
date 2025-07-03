import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

mpg = data[:, 0]
cyl = data[:, 1]
hp = data[:, 2]
wt = data[:, 3]

plt.scatter(hp, mpg, c='purple', s=wt*12, cmap='plasma', alpha=0.6)
plt.xlabel('Konjske snage (hp)')
plt.ylabel('Potrošnja goriva (mpg)')
plt.title('Potrošnja goriva vs. Konjske snage')
plt.colorbar(label='Težina vozila (wt)')
plt.show()

print("Minimalna potrošnja goriva (mpg):", np.min(mpg))
print("Maksimalna potrošnja goriva (mpg):", np.max(mpg))
print("Srednja potrošnja goriva (mpg):", np.mean(mpg))

mpg_6_cyl = mpg[cyl == 6]

print("Minimalna potrošnja goriva za automobile sa 6 cilindara:", np.min(mpg_6_cyl))
print("Maksimalna potrošnja goriva za automobile sa 6 cilindara:", np.max(mpg_6_cyl))
print("Srednja potrošnja goriva za automobile sa 6 cilindara:", np.mean(mpg_6_cyl))
