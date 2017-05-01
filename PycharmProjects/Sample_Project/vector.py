import numpy as np


def func(a, b):
    if a > b:
        return a - b
    else:
        return b - a


# print func(8,6)  #2  =(8-6)
# print func([1,4,3,6],5)   #Error

vect_func = np.vectorize(func)

print vect_func([1, 4, 3, 6], 5)  # [4 1 2 1]

print vect_func(5, [1, 4, 3, 6])  # [4 1 2 1]
