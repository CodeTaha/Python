try:
    a = int("asd123")
    print("Program burada")
except:
    print("Bir Hata Oluştu")
print("Bloklar Sona Erdi")

try:
    a = int("123")
    print("Program burada")
except:
    print("Bir Hata Oluştu")
print("Bloklar Sona Erdi")

try:
    a = int("asd123")
    print("Program burada")
except ValueError:
    print("Bir Hata Oluştu")
print("Bloklar Sona Erdi")

try:
    a = int(input("Sayı 1: "))
    b = int(input("Sayı 2: "))
    print(a / b)
except ValueError:
    print("Lütfen Doğru input Girin.")
except ZeroDivisionError:
    print("Bir Sayı Sıfıra Bölünemez")
print("Bloklar Sona Erdi")

try:
    a = int(input("Sayı 1: "))
    b = int(input("Sayı 2: "))
    print(a / b)
except ValueError:
    print("Lütfen Doğru input Girin.")
except ZeroDivisionError:
    print("Bir Sayı Sıfıra Bölünemez")
finally:
    print("Burası Çalıştı")
print("Bloklar Sona Erdi")

def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen string bir değer gönderin")
    else:
        return s[::-1]
print(terscevir(5))

try:
    print(terscevir(512))
except ValueError:
    print("Lütfen string bir değer gönderin")