lista = []

while True:
    unos = input("Unesite broj (ili 'done' za završetak): ")
    
    if unos.lower() == "done":
        break

    try:
        broj = int(unos)
        lista.append(broj)
    except ValueError:
        print("Pogrešan unos. Molimo unesite broj.")

# Provjerimo je li lista prazna
if lista:
    print(f"Uneseno brojeva: {len(lista)}")
    print(f"Maksimalna vrijednost: {max(lista)}")
    print(f"Minimalna vrijednost: {min(lista)}")
    print(f"Srednja vrijednost: {sum(lista) / len(lista)}")
    
    lista.sort()
    print(f"Sortirana lista: {lista}")
else:
    print("Nema unesenih brojeva.")
