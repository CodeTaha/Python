def ekstra_ozellik(func):
    def wrapper(sayilar):
        ciftler_toplami = 0
        tekler_toplami = 0
        cift_sayilar = list()
        tek_sayilar = list()

        for i in sayilar:
            if(i % 2 == 0):
                ciftler_toplami += i
                cift_sayilar.append(i)
            else:
                tekler_toplami += i
                tek_sayilar.append(i)
        print("Çift sayıların Toplamı: " , ciftler_toplami , "\nÇift sayıların listesi: " , cift_sayilar ,"\nÇift sayıların ortalaması: " , ciftler_toplami/len(cift_sayilar) , "\nTek sayıların toplamı: " , tekler_toplami , "\nTek sayıların listesi: " , tek_sayilar , "\nTek sayıların ortalaması: " , tekler_toplami/len(tek_sayilar))
        func(sayilar)
    return wrapper
@ekstra_ozellik
def ortalamabul(sayilar):
    toplam = 0

    for i in sayilar:
        toplam += i
    print("Genel Ortalama: ",toplam/len(sayilar))

ortalamabul([1,2,3,4,15,66,134,33,25])