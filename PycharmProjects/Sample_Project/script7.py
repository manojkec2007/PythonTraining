"""
7. Write a program to reverse/inverse key:value like below. 
dict1 = { 'a': 1, 'b':2 } 
Expected result : dict2 = { 1: 'a', 2: 'b' }
"""

dict1 = { 'a': 1, 'b':2 }
dict2 = {v:k for k,v in dict1.items()}

print "Expected result: dict2 = ", dict2