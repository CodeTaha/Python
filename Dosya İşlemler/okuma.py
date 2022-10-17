file = open("bilgiler.txt", "r", encoding = "utf-8")
file.close()

try:
    file = open("bilgiler2.txt", "r")
except FileNotFoundError:
    print("Dosya Bulunamadı...\n")

file = open("bilgiler.txt", "r", encoding = "utf-8")
for i in file:
    print(i, end = "")
print("")
file.close()

file = open("bilgiler.txt", "r", encoding = "utf-8")
icerik = file.read()
print("Dosyanın İçeriği: ")
print(icerik)
file.close()

file = open("bilgiler.txt", "r", encoding = "utf-8")
print(file.readline(), end = "")
print(file.readline(), end = "")
print(file.readline(), end = "")
print(file.readline(), end = "")
file.close()

file = open("bilgiler.txt", "r", encoding = "utf-8")

liste = file.readlines()
print(liste)
file.close()