print("""******************************
Kullanıcı Girişi Programı
******************************
""")
data_kul_adi = "konyartaha1905"
data_sifre = "123456"

kul_adi = input("Kullanıcı Adınızı Giriniz: ")
sifre = input("Şifrenizi Giriniz: ")

if(data_kul_adi == kul_adi and data_sifre == sifre):
    print("Hoşgeldin {}".format(kul_adi))
elif(data_kul_adi != kul_adi and data_sifre == sifre):
    print("Kullanıcı Adı Bulunamadı.")
elif(data_kul_adi == kul_adi and data_sifre != sifre):
    print("Hatalı Şifre.")
else:
    print("Kullanıcı adı ve şifre hatalı.")