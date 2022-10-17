with open("bilgiler.txt", "r+", encoding = "utf-8") as file:
    file.seek(11)
    file.write("Deneme")

with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt", "a", encoding ="utf-8") as file:
    file.write("Mustafa Berken\n")

with open("bilgiler.txt", "r+", encoding ="utf-8") as file:
    file.write("Mustafa Berken\n")