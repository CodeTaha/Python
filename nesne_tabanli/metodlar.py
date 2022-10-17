class yazılımcı():

    def __init__(self, isim, soyisim, maas, numara, dilleri):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.numara = numara
        self.dilleri = dilleri

    def bilgileri_goster(self):
        print("""
        Yazılımcı objesinin özellikleri
        İsim: {}
        Soyisim: {}
        Maaş: {}
        Numara: {}
        Bildiği Dilleri: {}  
        """.format(self.isim, self.soyisim, self.maas, self.numara, self.dilleri))

    def zam_yap(self, zam):
        self.zam = zam
        self.maas += zam

    def dil_ekle(self, dil):
        self.dil = dil
        self.dilleri.append(dil)

yazılımcı1 = yazılımcı("Recep Taha", "Konyar", 15000, 905526632755, ["Java", "Python"])
print(yazılımcı1.bilgileri_goster())
yazılımcı1.zam_yap(3000)
print(yazılımcı1.bilgileri_goster())
yazılımcı1.dil_ekle("Javascript")
print(yazılımcı1.bilgileri_goster())