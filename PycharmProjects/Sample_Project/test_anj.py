
"""
x = range(3)
print x

y = enumerate(range(3))
print y

"""

"""
import datetime

print datetime.datetime.now()
test = (lambda: datetime.datetime(2012, 12, 12))
print test

"""
"""
a = 'Manoj'
print type(a) # string
b = a.split('a')
print b
print type(b) # list
c = list(a)
print c
print type(c) # list

d = a[::-1]
print d  # 'jonaM'
print type(d) # string

"""

"""
a = [1,2,3]
# a.append([4,5,6])
# a.extend([4,5,6])
a.insert(2,4)
print a  # 1,2,4,3
a.pop(2) #  index(position) it wil remove the 3rd element
print a  # 1,2,3
a.remove(3) # value
print a  # 1,2
del a[1]
print a
"""

"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

"""

"""
str = 'manoj'
int(str)
"""

2
3
4
5
6
7
8
9
10
11

"""
def extendList(val, list=[]):
    list.append(val)
    return list


list1=extendList(10)
list2=extendList(123, [])
list3=extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

"""
"""
import os
print (os.path.expanduser('~'))

"""

"""
import re
print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"))

"""
