class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

kitap = Kitap("Sefiller", "Victor Hugo", 533, "Macera, Dram")
print(kitap)

class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        print("str fonksiyonu")
        return  "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim, self.yazar, self.sayfa_sayisi, self.tur)

kitap = Kitap("Sefiller", "Victor Hugo", 533, "Macera, Dram")
print(kitap)

class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        return  "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim, self.yazar, self.sayfa_sayisi, self.tur)
    def __len__(self):
        print("len fonksiyonu")
        return self.sayfa_sayisi

kitap = Kitap("Sefiller", "Victor Hugo", 533, "Macera, Dram")
print(len(kitap))

class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        return  "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim, self.yazar, self.sayfa_sayisi, self.tur)
    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("del fonksyonu")
        print("Kitap objesi siliniyor...")

kitap = Kitap("Sefiller", "Victor Hugo", 533, "Macera, Dram")
del kitap