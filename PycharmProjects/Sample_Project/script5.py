"""
5. Write a for loop that prints all elements of a list and their position in the list. 
a = [4,7,3,2,5,9]
"""

a = [4,7,3,2,5,9]
print "The Given List is",a

print 'The Elements of the list and their positions are as follows'
for i in a:
    print "Element ",str(i)+" is at "+str(a.index(i)+1)+" position"
