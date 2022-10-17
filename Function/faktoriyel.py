def faktoriyel(sayi):
    fakt = 1
    if sayi == 0 or sayi == 1:
        print("faktoriyel= ", fakt)
    else:
        while sayi >= 1:
            fakt *= sayi
            sayi -= 1
        print(fakt)

faktoriyel(5)