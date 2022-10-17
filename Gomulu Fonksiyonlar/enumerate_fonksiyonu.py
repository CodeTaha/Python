liste = ["Elma", "Armut", "Muz", "Kiraz"]
i = 0
sonuc = list()

while(i < len(liste)):
    sonuc.append((i,liste[i]))
    i += 1
print(sonuc)

print(list(enumerate(liste)))

for i,j in enumerate(liste):
    print(i,j)

liste = ["a","b","c","d","e","f","g"]

for i,j in enumerate(liste):
    if (i % 2 == 0):
        print(j)