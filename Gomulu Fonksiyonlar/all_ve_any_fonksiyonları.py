def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste = [True, False, True, False, True]
print(hepsi(liste))

liste = [1,2,3,4,5,6]
print(hepsi(liste))

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

liste = [True, False, True, False, True]
print(herhangi(liste))

liste = [0,0,0,0,0,0]
print(herhangi(liste))

liste = [True, False, True, False, True]
print(all(liste))

liste = [1,2,3,4,5,6]
print(all(liste))

liste = [True, False, True, False, True]
print(any(liste))

liste = [0,0,0,0,0,0]
print(all(liste))