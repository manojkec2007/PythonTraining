1. Write a program to print the:
a. Number of lowercase “a” and “o” in the following sentence.
b. Number of uppercase “L” and “N” in the following sentence.
‘Discover, Learning, with, Edureka’

Answer:
>>> input_str = 'Discover, Learning, with, Edureka'
>>> input_str
'Discover, Learning, with, Edureka'
>>> a_count = input_str.count('a')
>>> o_count = input_str.count('o')
>>> L_count = input_str.count('L')
>>> N_count = input_str.count('N')
>>>
>>> a_count
2
>>> o_count
1
>>> L_count
1
>>> N_count
0
>>>
####################################

2. Write a program to remove the following from:
www.edureka.in
a. Remove all w’s before and after .edureka.
b. Remove all lowercase letter before and after .edureka.
c. Remove all printable characters

Answer:

>>> input_str = 'www.edureka.in'
>>> match_str = '.edureka.'
>>> if match_str in input_str:
...     print input_str.strip('w')
...     print input_str.strip(string.lowercase)
...     print input_str.strip(string.printable)
... else:
...     print "Wrong Match"
...
.edureka.in
.edureka.

>>>

####################################

3. Identify the type of numbers:
a. 0X7AE
b. 3+4j
c. -01234
d. 3.14e-2

Answer:
>>> type(0X7AE)    # Hexa Decimal Value
<type 'int'>
>>>
>>> type(3+4j)
<type 'complex'>
>>>
>>> type(-01234)    # Octal Decimal Value
<type 'int'>
>>>
>>> type(3.14e-2)
<type 'float'>
>>>
####################################

4. Write a program for String Formatting Operator % which should
include the following conversions:
a. Character
b. Signed decimal integer
c. Octal integer
d. Hexadecimal integer (UPPERcase letters)
e. Floating point real number
f. Exponential notation (with lowercase 'e')

Answer:

>>> char = 'Manoj'
>>> signed_int = 1234
>>> octal_int = 030
>>> hexa_int =  0X30
>>> float_num = 16.52
>>> expon_not = 1.652e1
>>>
>>>
>>> print "Employee Name    is %s" %(char)
Employee Name    is Manoj
>>> print "Employee ID      is %d" %(signed_int)
Employee ID      is 1234
>>> print "Department ID    is %o" %(octal_int)
Department ID    is 30
>>> print "Department Name  is %X" %(hexa_int)
Department Name  is 30
>>> print "Salary in USD'   is %f" %(float_num)
Salary in USD'   is 16.520000
>>> print "Salary in Expon' is %e" %(expon_not)
Salary in Expon' is 1.652000e+01
>>>
####################################