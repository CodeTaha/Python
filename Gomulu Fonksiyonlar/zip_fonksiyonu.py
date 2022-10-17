liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
liste3 = ["Java","Python","Php","C","C#"]

i = 0
sonuc = list()
while(i < len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i += 1
print(sonuc)
print(list(zip(liste1,liste2,liste3)))

liste1 = [1,2,3,4]
liste2 = ["Java","Python","Php","C#"]

for i,j in zip(liste1,liste2):
    print(i,j)

dict1 = {"Elma":1,"Armut":2,"Kiraz":3}
dict2 = {"Sıfır":0,"Bir":1,"İki":2}

print(list(zip(dict1,dict2)))
print(list(zip(dict1.values(),dict2.values())))