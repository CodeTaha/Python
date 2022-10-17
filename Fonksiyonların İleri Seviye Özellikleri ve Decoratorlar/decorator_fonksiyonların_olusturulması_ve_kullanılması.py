import time
def zaman_hesapla(func):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = func(sayilar)
        bitis = time.time()
        print(func.__name__+" "+str(bitis-baslama)+" saniye sürdü.")
        return sonuc
    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i ** 2)
    return sonuc
@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i ** 3)
    return sonuc
kareleri_hesapla(range(10000000))
kupleri_hesapla(range(10000000))