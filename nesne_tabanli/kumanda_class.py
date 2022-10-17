import random
import time

class Kumanda():

    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["TRT"], kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum = "Açık"
            time.sleep(5)
            print("Televizyon Açıldı")

    def tv_kapat(self):
        if ( self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon Kapatılıyor")
            self.tv_durum = "Kapalı"
            time.sleep(5)
            print("Televizyon Kapatıldı")

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Aç: '>'\nÇıkış: 'q'\n")

            if (cevap == "<" and self.tv_ses != 0):
                self.tv_ses -= 1
                print("Ses: ", self.tv_ses)
            elif (cevap == ">" and self.tv_ses != 10):
                self.tv_ses += 1
                print("Ses: ", self.tv_ses)
            elif (cevap == "q"):
                print("Ses Güncellendi...", self.tv_ses)
                time.sleep(1)
                break
            else:
                ("Yanlış giris yaptınız")

    def kanal_ekle(self, kanal_ismi):
        self.kanal_listesi.append(kanal_ismi)

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu Anki Kanal: ", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv ses: {}\nKanal Listesi: {}\nŞu Anki Kanal: {}".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)
kumanda = Kumanda()

print("""
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanal Geçme
7. Televizyon Bilgileri

Çıkmak İçin 'e' ye basın.
""")
while True:
    islem = input("İşlemi giriniz:")

    if (islem == "e"):
        print("Program Sonlandırılıyor...\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Program Sonlandırıldı...")
        break
    elif (islem == "1"):
        time.sleep(1)
        kumanda.tv_ac()
    elif (islem == "2"):
        time.sleep(1)
        kumanda.tv_kapat()
    elif (islem == "3"):
        time.sleep(1)
        kumanda.ses_ayarlari()
    elif (islem == "4"):
        time.sleep(1)
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (islem == "5"):
        time.sleep(1)
        print("Kanal Sayısı: ",len(kumanda))
    elif (islem == "6"):
        time.sleep(1)
        kumanda.rastgele_kanal()
    elif (islem == "7"):
        time.sleep(1)
        print(kumanda)
    else:
        print("Yanlış giriş yaptınız...")