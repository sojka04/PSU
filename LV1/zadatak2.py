try:
    ocjena = float(input("Unesite ocjenu (float) između 0.0 i 1.0: "))
    if 0.0 <= ocjena <= 1.0:
        if ocjena >= 0.9:
            print('A')
        elif ocjena >= 0.8:
            print('B')
        elif ocjena >= 0.7:
            print('C')
        elif ocjena >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print("Greška: Ocjena je izvan dozvoljenog raspona.")
except ValueError:
    print("Greška: Unesite validan broj u formatu float.")
