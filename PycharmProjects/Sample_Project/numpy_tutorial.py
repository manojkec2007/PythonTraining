import numpy as np
import time
import sys


"""
# Less memory
l = range(1000)
print sys.getsizeof(5)*len(l)  # 24000 # 1 object =14 bytes

array = np.arange(1000)
print (array.size*array.itemsize) # 4000  1 element 4 bytes
"""

# Fast
size = 1000000 

l1 = range(size)
l2 = range(size)

a1= np.arange(size)
a2= np.arange(size)

# Python list
start = time.time()
result = [(x+y) for x,y in zip(l1, l2)]
print "Python list took:", (time.time()-start)*1000  # Python list took: 289.999961853

# numpy array
start = time.time()
result = a1+a2
print "Numpy array took:", (time.time()-start)*1000  # Numpy array took: 6.99996948242
