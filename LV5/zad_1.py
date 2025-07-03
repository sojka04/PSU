import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

podaci = pd.read_csv('occupancy_processed.csv')
print(f'Broj primjera u skupu podataka: {len(podaci)}')

znacajke = ['S3_Temp', 'S5_CO2']
ciljna_varijabla = 'Room_Occupancy_Count'
klase = ['Slobodna', 'Zauzeta']

X = podaci[znacajke].to_numpy()
y = podaci[ciljna_varijabla].to_numpy()

plt.figure(figsize=(8, 6))
boje = ['skyblue', 'salmon']

for vrijednost_klase in np.unique(y):
    maska = y == vrijednost_klase
    plt.scatter(
        X[maska, 0],
        X[maska, 1],
        c=boje[vrijednost_klase],
        label=klase[vrijednost_klase],
        edgecolors='k',
        alpha=0.7
    )

plt.xlabel('Temperatura (S3_Temp)')
plt.ylabel('CO2 razina (S5_CO2)')
plt.title('Vizualizacija zauzetosti prostorije')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
