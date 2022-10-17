with open("bilgiler.txt", "r", encoding = "utf-8") as file:
    print(file.tell())
    file.seek(0)
    print(file.tell())