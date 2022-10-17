class araba():
    model = "Mazda RX7"
    renk = "Siyah"
    beygir_gucu = 1200
    silindir = 6
    def __init__(self):
        print("init fonksiyonu çağırıldı")
araba1 = araba()
araba2 = araba()
print(araba1.model)
print(araba2.beygir_gucu)
print(araba.renk)
print(dir(araba))
araba()

class araba():
    def __init__(self, model = "Bilgi Yok", renk = "Bilgi Yok", beygir_gucu = "Bilgi Yok", silindir = "Bilgi Yok"):
        print("init fonksiyonu çağrıldı")
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir

araba1 = araba("Mazda RX7", "Siyah", 1200, 6)
araba2 = araba("Peguot Partner", "Beyaz", 110, 2)
araba3 = araba("Wolksvagen Golf MK2", "Sarı", 550)
araba3 = araba(beygir_gucu = 330)
print(araba1.model)
print(araba2.model)
print(araba3.silindir)
print(araba3.beygir_gucu)