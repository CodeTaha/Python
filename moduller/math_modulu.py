from math import floor,ceil,factorial

print(factorial(5))
print(ceil(6.3))
print(floor(6.3))

def factoriel(sayi):
    print("benim fonksiyonum")

    faktoriyel = 1
    if sayi == 0 or sayi == 1:
        return 1
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        return faktoriyel
print(factoriel(5))