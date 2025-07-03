import pandas as pd

mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\LV3\\mtcars.csv.csv')

print("Top 5 automobila s najvećom potrošnjom:")
print(mtcars.sort_values(by='mpg', ascending=False).head(5))

print("\nTri automobila s 8 cilindara i najmanjom potrošnjom:")
print(mtcars[mtcars.cyl == 8].sort_values(by='mpg').head(3))

cyl6 = mtcars[mtcars.cyl == 6]
total_mpg_6cyl = cyl6['mpg'].sum()
count_6cyl = cyl6['mpg'].count()
average_mpg_6cyl = total_mpg_6cyl / count_6cyl
print(f"Srednja potrošnja automobila sa 6 cilindara: {average_mpg_6cyl:.2f}")

car4 = mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2.000) & (mtcars.wt < 2.200)]
total_mpg_4cyl_weight = car4['mpg'].sum()
count_4cyl_weight = car4['mpg'].count()
average_mpg_4cyl_weight = total_mpg_4cyl_weight / count_4cyl_weight
print(f"Srednja potrošnja automobila s 4 cilindra i masom između 2000 i 2200 lbs: {average_mpg_4cyl_weight:.2f}")

manual_count = mtcars[mtcars.am == 0].shape[0]
auto_count = mtcars[mtcars.am == 1].shape[0]
print(f"\nBroj automobila s ručnim mjenjačem: {manual_count}, s automatskim mjenjačem: {auto_count}")

car_auto_hp = mtcars[(mtcars.am == 1) & (mtcars.hp > 100)]
print(f"\nBroj automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga: {len(car_auto_hp)}")

mtcars['wt_kg'] = mtcars['wt'] * 1000 / 2.20462262
print("\nMasa svakog automobila u kilogramima:")
print(mtcars[['wt', 'wt_kg']])
