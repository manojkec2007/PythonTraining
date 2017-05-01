# 1 . Class and Instance Creation
"""
class Employee:  # Employee Class
    pass

emp1 = Employee()  # instance 1
emp2 = Employee()  # instance 2

print emp1  # <__main__.Employee instance at 0x0000000001FD5408>
print emp2  # <__main__.Employee instance at 0x000000000276FD08>
"""
# 2 . Instance Variables  Creation

"""
class Employee:  # Employee Class
    pass

emp1 = Employee()  # instance 1
emp2 = Employee()  # instance 2

print emp1  # <__main__.Employee instance at 0x0000000001FD5408>
print emp2  # <__main__.Employee instance at 0x000000000276FD08>

emp1.fname = 'Manoj'
emp1.lname = 'KV'
emp1.email = 'Manoj.KV@company.com'
emp1.pay = 50000

emp2.fname = 'Raj'
emp2.lname = 'Kumar'
emp2.email = 'Raj.Kumar@company.com'
emp2.pay = 60000

print emp1.email  # Manoj.KV@company.com
print emp2.email  # Raj.Kumar@company.com

"""

# 3 . Class Members Creation

class Employee:  # Employee Class
    def __init__(self,fname,lname,pay)
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname




