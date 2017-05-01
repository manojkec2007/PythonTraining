import numpy as np
arr1 = np.array([1,2,0,4])
print arr1
arr2 =arr1.copy() +1
print arr2
arr3=arr1.view()
print arr3
print arr1/arr3

print dir(arr1)
