"""
6. Write a program which should create a dictionary of key:values. 
'A':1 'B':2 'C':3 . . . . 'Z':26 [Use dictionary comprehension]
"""

import string
from operator import itemgetter
dict = {}  # empty dictionary
input = string.uppercase[:26]
dict = {str(i): int(input.index(i) + 1) for i in input}
print dict
