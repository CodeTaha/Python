d = 10

def globald():

    global d
    d = 5
    print(d)

globald()
print(d)