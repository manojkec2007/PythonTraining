
"""
#1 Iterative:

def fibonacci(n):
    terms=[0,1]
    i = 2
    while i <= n:
        terms.append(terms[i-1]+terms[i-2])
        i+=1
    return terms[n]

number = input("Enter a value: ")
# print number

fibo = fibonacci(number)
print fibo
"""

"""
#2. Recursive
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

number = input("Enter a value: ")
# print number

fibo = fibonacci(number)
print fibo
"""

#3 Sequence :

a,b = 0,1

for i in xrange(0,10):
    print a
    a,b=b,a+b

