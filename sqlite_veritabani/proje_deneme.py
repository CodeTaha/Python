from kutuphane_projesi import *

print("""***********************************
Kütüphane Programına Hoşgeldiniz.
İşlemler;
1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
Çıkmak İçin 'q' ya basın.
***********************************
""")
kutuphane_projesi = Kutuphane()
while True:
    islem = input("Yapacağınız İşlem: ")

    if (islem == "q"):
        print("Program Sonlandırılıyor...")
        time.sleep(2)
        print("Yine Bekleriz")
        break
    elif (islem == "1"):
        time.sleep(1)
        kutuphane_projesi.kitaplari_goster()
    elif (islem == "2"):
        isim = input("Hangi Kitabı İstiyorsunuz?: ")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)
        kutuphane_projesi.kitap_sorgula(isim)
    elif (islem == "3"):
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Tür: ")
        baski = input("Baskı: ")
        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap Ekleniyor...")
        time.sleep(2)
        kutuphane_projesi.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi")
    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz: ")
        print("Kitap siliniyor...")
        time.sleep(2)
        kutuphane_projesi.kitap_sil(isim)
        print("Kitap Silindi")
    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz: ")
        print("Baskı Yükseltiliyor")
        time.sleep(1)
        kutuphane_projesi.baski_yukselt(isim)
    else:
        print("Geçersiz İşlem")
