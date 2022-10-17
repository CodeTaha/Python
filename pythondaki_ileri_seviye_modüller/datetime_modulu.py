from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")
su_an = datetime.now()
print(su_an)
print(su_an.year)
print(datetime.ctime(su_an))
print(datetime.strftime(su_an,"%B %Y"))
saniye = datetime.timestamp(su_an)
print(saniye)
su_an2 = datetime.fromtimestamp(saniye)
print(su_an2)
tarih = datetime(2002,9,8,23)
su_an = datetime.now()
print(su_an-tarih)