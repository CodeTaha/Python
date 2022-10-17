import time
def fonksiyon(*args):
    for i in args:
        print(i)
fonksiyon(1,2,3)
fonksiyon(1,2,3,4,5,6,7)
def fonksiyon(isim,*args):
    print("İsim:",isim)
    print("---------------")
    for i in args:
        print(i)
fonksiyon("Taha","Recep",1,2,3,4,5,6,7)

def fonksiyon(**kwargs):
    print(kwargs)
fonksiyon(isim = "Taha",soyisim = "Konyar",numara = "1001")

def fonksiyon(**kwargs):
    for i,j in kwargs.items():
        print("Argüman İsmi",i,"Argüman Değeri",j)
fonksiyon(isim = "Recep Taha",soyisim = "Konyar",numara = "1001")

def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)
    print("--------------")
    for i,j in kwargs.items():
        print(i,j)
fonksiyon(1,2,3,4,5,6,isim = "Recep Taha",soyisim = "Konyar",numara = "1001")

def selamla(isim):
    print("Selam",isim)
selamla("Taha")
merhaba = selamla
del selamla
merhaba("Taha")

def fonksiyon():
    def fonksiyon2():
        print("Küçük fonksiyondan herkese merhaba")
        time.sleep(1)
    fonksiyon2()
    print("Büyük fonksiyondan herkese merhaba")
fonksiyon()

def fonksiyon(*args):
    def toplama(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(toplama(args))
fonksiyon(1,2,3,4,5,6)