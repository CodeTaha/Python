x = {1,2,3}
print(type(x))

x = set()

liste = [1,2,3,3,1,1,2,2,2]
x = set(liste)
print(type(x))
print(x)

x = set("Python programlama dili")
print(x)

x = {"Python","Php","Python"}
print(x)

x = {"Elma","Armut","Kiraz","Muz"}
for i in x:
    print(i)

x = {"Python","Php","Java","Javascript"}

liste = list(x)
print(liste[0])

for i in liste:
    print(i)

x = {1,2,3,4,5}
x.add(6)#eklenen elemanın diğer elemanlardan farklı olması gerekir yoksa yeni eleman eklenmez
print(x)

kume1 = {1,2,3,4,5,6,7,8,9}
kume2 = {3,0,-1,12,6,9,7}
print(kume1.difference(kume2))#küme1 in küme2 den farkı
print(kume2.difference(kume1))
kume1.difference_update(kume2)#küme1 in küme2 den farkını alıp küme1 i değiştirir
print(kume1)

x = {1,2,3,4,5,6}
x.discard(4)#kümeden elemanı çıkarır eğer eleman yoksa etkisi olmaz
print(x)

kume1 = {1,2,3,4,5,6,7,8,9}
kume2 = {3,0,-1,12,6,9,7}
print(kume1.intersection(kume2))#küme1 ve küme2 nin kesişimlerini gösterir
kume1.intersection_update(kume2)#kesişimleri kümeye uygular
print(kume1)
kume2.intersection_update(kume1)
print(kume2)

kume1 = {1,2,3,4,5,6,7,8,9}
kume2 = {3,0,-1,12,6,9,7}
kume3 = {13,25,33,555,44,18}
print(kume1.isdisjoint(kume3))#kümeler ayrık küme mi diye sorar ve bool çıktı verir (ayrık küme: hiçbir ortak elemeanı olmayan küme.)
print(kume1.issubset(kume1))#bir küme diğerinin alt kümesi mi diye sorar buna göre bool çıktı verir (alt küme: bir kümenin tüm elemanları ile ortak olan ve o kümeye eşit veya daha az elamanlı küme)
print(kume1.union(kume2.union(kume3)))#tüm kümeleri ortak kümeye alır

kume2.update(kume3)#bir kümeyi diğer kümeyle ortak kümeye alır
kume1.update(kume2)
print(kume1)