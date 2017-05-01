"""
8. Using given list L = ['a', 'b', 'c', 'd'] create a dictionary of key:values.
Expected result {'a': 1, 'c': 3, 'b': 2, 'd': 4} [Hint: Use Enumerate function]
"""
L = ['a', 'b', 'c', 'd']
dict = dict(enumerate(L))
dict2 = {v:k+1 for k,v in dict.items()}
print "Expected result: ",dict2
