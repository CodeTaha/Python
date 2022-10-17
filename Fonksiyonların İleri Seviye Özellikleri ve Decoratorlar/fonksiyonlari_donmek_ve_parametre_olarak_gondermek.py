def anafonksiyon(islem_adi):

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpim(*args):
        carp = 1
        for i in args:
            carp *= i
        return carp
    if islem_adi == "toplama":
        return toplama
    else:
        return carpim

fonk = anafonksiyon("toplama")
print(fonk(1,2,3,44))
fonk1 = anafonksiyon("carpim")
print(fonk1(1,2,3,4,5))

def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a - b
def carpma(a,b):
    return a * b
def bolme(a,b):
    return a / b

def anafonksiyon(func1,func2,func3,func4,islem_adi):

    if islem_adi == "toplama":
        print(func1(3,4))
    elif islem_adi == "çıkarma":
        print(func2(10,3))
    elif islem_adi == "çarpma":
        print(func3(3,5))
    elif islem_adi == "bölme":
        print(func4(10,4))
    else:
        print("Geçersiz İşlem...")

anafonksiyon(toplama,cikarma,carpma,bolme,"bölme")