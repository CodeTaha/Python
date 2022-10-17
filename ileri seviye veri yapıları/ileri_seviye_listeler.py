liste = [1,2,3,4,5]
liste.append(6)
liste.append("Python")
print(liste)

liste1 = [1,2,3,4,5,6,7]
liste2 = [1,2,3,"Php",11,12]
liste1.extend(liste2)#listeleri birbirine yapıştırır ama kümelerin aksine aynı elemandan birden fazla olabilir
print(liste1)

liste = [1,2,3,4,5,6,7,8,9]
liste.insert(0,"Java")
liste.insert(2,("Python"))#append metodunda listenin sonuna eklenir fakat insert ile hangi indexe ekleneceğini seçebilirsiniz
print(liste)

liste = [1,2,3,4,5,6,7]
print(liste.pop())#hiçbir değer girilmez ise sondaki elemanı silip silinen elemanı ekrana yazar
print(liste)
print(liste.pop(2))#girdiğiniz index silinip ekrana yazılır
print(liste)

liste = ["Python","Java","Javascipt","Php","C","C++","C#"]
liste.remove("Java")#girilen değer listemizde varsa siler yoksa hataverir
print(liste)
liste.remove("Python")
print(liste)

liste = [1,2,3,4,3,3,5,3,6,7,8,9]
print(liste.index(3))#girdiğimiz değerin kaçıncı indexte olduğunu arar eğer eleman yoksa hata verir
print(liste.index(3,3))#x.index((aradığımız değer),(aramaya başlamasını istediğimiz index))
print(liste.count(3))#verilen değerin listede kaç defa geçtiğini sayar
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)

liste = ["Python","Java","Javascipt","Php","C","C++","C#"]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)