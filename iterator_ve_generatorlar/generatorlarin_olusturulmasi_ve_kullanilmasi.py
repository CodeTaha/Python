def karelerial():
    sonuc = []

    for i in range(1,6):
        sonuc.append(i ** 2)
    return sonuc
print(karelerial())

def karelerial():
    for i in range(1,6):
        yield i ** 2

generator = karelerial()
iterator = iter(generator)

for i in iterator:
    print(i)

liste = [i * 3 for i in range(5)]
print(liste)
generator = (i * 3 for i in range(5))
for i in generator:
    print(i)

def carpim_tablosu():
    for i in range(1,11):
        print("\n")
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpim_tablosu():
    print(i)