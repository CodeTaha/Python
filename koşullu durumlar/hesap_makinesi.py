print("""******************************
Hesap Makinesi Programı

İşlemler;

1-) Toplama
2-) Çıkarma
3-) Çarpma
4-) Bölme
******************************
""")
islem = input("Yapılacak İşlemi Seçiniz: ")
a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı: "))

if(islem == "1"):
    print(a + b)
elif(islem == "2"):
    print(a - b)
elif(islem == "3"):
    print(a * b)
elif(islem == "4"):
    print(a / b)
else:
    print("Geçersiz İşlem")