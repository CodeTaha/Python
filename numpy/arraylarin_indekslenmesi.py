import numpy as np

arr = np.arange(1,11)
print(arr)
print(arr[2])
print(arr[0:5])

arr[7:10] = 25
print(arr)

arr = np.arange(0,11)
arr2 = arr
arr2[:3] = 11
print(arr2)
print(arr)

arr = np.arange(0,11)
arr2 = arr.copy()
arr2[:3] = 11
print(arr2)
print(arr)

newArray = np.arange(1,21)
newArray.reshape(5,4)
print(newArray)
newArray = newArray.reshape(5,4)
print(newArray)
print(newArray[:,:2])
print(newArray[:2,:2])
print(newArray[:2,:])
print(newArray[:2])

arr = np.arange(1,11)
print(arr > 3)

booleanArray = arr > 3
print(arr[booleanArray])