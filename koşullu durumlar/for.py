liste = [(1,2),(3,4),(5,6),(7,8)]

for i in liste:
    for j in i:
        print(j)
for (i,j) in liste:
    print("i: {} j: {}".format(i,j))