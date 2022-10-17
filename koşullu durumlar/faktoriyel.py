a = int(input("Fkatöriyelini bulmak istediğiniz sayıyı giriniz: "))
faktoriyel = 1
for i in range(2, a+1):
    faktoriyel *= i
print(faktoriyel)