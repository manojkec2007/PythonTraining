
# iterative type:
number = input("Enter a non-negative Integer: ")
# print number


def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i+1)
    return product

fact = factorial(number)
print fact

"""

# Recursive:
def factorial(number):
    if number <=1:
        return 1
    else:
        return number * factorial(number -1)


input_num = input("Enter a non-negative Integer: ")
# print number

fact = factorial(input_num)
print fact

"""