import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\LV3\\mtcars.csv.csv')

plt.figure(figsize=(10, 6))
cylinders = mtcars['cyl'].unique()
mpg_by_cyl = [mtcars[mtcars['cyl'] == cyl]['mpg'].mean() for cyl in cylinders]
plt.bar(cylinders, mpg_by_cyl, color=['blue', 'green', 'red'])
plt.title('Potrošnja automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Prosječna potrošnja (mpg)')
plt.show()

plt.figure(figsize=(10, 6))
mtcars.boxplot(column='wt', by='cyl', patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'))
plt.title('Distribucija težine automobila s 4, 6 i 8 cilindara')
plt.suptitle('')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (1000 lbs)')
plt.show()

plt.figure(figsize=(10, 6))
manual_cars = mtcars[mtcars['am'] == 0]
auto_cars = mtcars[mtcars['am'] == 1]
plt.scatter(manual_cars['mpg'], manual_cars['am'], color='red', label='Ručni mjenjač')
plt.scatter(auto_cars['mpg'], auto_cars['am'], color='blue', label='Automatski mjenjač')
plt.title('Potrošnja automobila s ručnim i automatskim mjenjačem')
plt.xlabel('Potrošnja (mpg)')
plt.ylabel('Vrsta mjenjača (0=ručni, 1=automatski)')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(manual_cars['qsec'], manual_cars['hp'], color='red', label='Ručni mjenjač')
plt.scatter(auto_cars['qsec'], auto_cars['hp'], color='blue', label='Automatski mjenjač')
plt.title('Odnos ubrzanja i snage automobila')
plt.xlabel('Ubrzanje (qsec)')
plt.ylabel('Snaga (hp)')
plt.legend()
plt.show()
