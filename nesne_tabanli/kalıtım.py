class Calısan():

    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri...")
        print("""
        isim: {}
        maaş: {}
        departman: {}
        """.format(self.isim, self.maas, self.departman))

    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calısan):
    pass

yonetici1 = Yonetici("Recep Taha Konyar", 3000, "Yazılım Mühendisliği")
print(yonetici1.bilgileri_goster())
yonetici1.departman_degistir("Veri Bilimi")
print(yonetici1.bilgileri_goster())
print(dir(yonetici1))

class Yonetici(Calısan):
    def zam_yap(self, zam_miktarı):
        self.maas += zam_miktarı

yonetici1 = Yonetici("Mustafa Berken Konyar", 4000, "Bilişim Teknolojileri")
yonetici1.zam_yap(500)
print(yonetici1.bilgileri_goster())