import numpy as np

data_list = [1,2,3]
print(data_list)

arr = np.array(data_list)
print(arr)

data_list2 = [[10,20,30],[40,50,60],[70,80,90]]
arr2 = np.array(data_list2)
print(arr2)

arr3 = np.array([1,2,3,4,5])
print(arr3)
print(arr3[3])
print(arr2[2][2])

print(np.arange(10,21))
print(np.arange(10,21,3))
print(np.zeros(8))
print(np.ones(3))
print(np.zeros((2,4)))

print(np.linspace(0,100,5))
print(np.linspace(0,79,4))

print(np.eye(6))
print(np.eye(3))

print(np.random.randint(11))
print(np.random.randint(10,21))

print(np.random.rand(5))#0-1 arası 5 rastgele sayı

print(np.random.randn(5))

arr = np.arange(25)
print(arr)

print(arr.reshape(5,5))

newArray = np.random.randint(1,100,10)
print(newArray)
print(newArray.max())
print(newArray.argmax())
print(newArray.min())
print(newArray.argmin())
print(newArray.sum())
print(newArray.mean())

detArray = np.random.randint(1,101,25)
detArray = detArray.reshape(5,5)
print(detArray)
print(np.linalg.det(detArray))
print(round(np.linalg.det(detArray)))

detArray2 = np.array([[1,2],[3,4]])
print(np.linalg.det(detArray2))
print(round(np.linalg.det(detArray2)))