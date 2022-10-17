print("""
****************
Kullanıcı girişi
****************
""")
data_kul_adi = "konyartaha1905"
data_sifre = "123456"
giris_hakki = 3
i = 1
while True:
    if i > giris_hakki:
        print("Giriş hakkınız kalmamıştır...")
        break
    kul_adi = input("Kullanıcı Adı giriniz: ")
    sifre = input("Şifre Giriniz: ")
    if(data_kul_adi == kul_adi and data_sifre == sifre):
        print("Hoşgeldiniz {}".format(kul_adi))
        break
    elif(data_kul_adi != kul_adi and data_sifre == sifre):
        print("Sizi tanıyamadık {}".format(kul_adi))
        i += 1
    elif(data_kul_adi == kul_adi and data_sifre != sifre):
        print("Girdiğiniz şifre yanlış")
        i += 1
    else:
        print("kullanıcı adı ve parola yanlış")
        i += 1