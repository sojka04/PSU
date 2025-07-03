spam_zbroj = 0
ham_zbroj = 0
spam_brojac = 0
ham_brojac = 0
usklicnik_brojac = 0

try:
    dat = open("C:\\Users\\student\\Desktop\\SMSSpamCollection.txt", 'r')
except:
    print("Datoteka ne postoji")

for linija in dat:
    linija = linija.split()
    if linija[0] == "ham":
        ham_brojac += 1
        ham_zbroj += len(linija)
    elif linija[0] == "spam":
        spam_brojac += 1
        spam_zbroj += len(linija)
        if "!" in linija[-1]:
            usklicnik_brojac += 1

print("Prosječan broj riječi u SMS porukama tipa ham:", ham_zbroj / ham_brojac)
print("Prosječan broj riječi u SMS porukama tipa spam:", spam_zbroj / spam_brojac)
print("Broj SMS poruka tipa spam koje završavaju sa '!':", usklicnik_brojac)
