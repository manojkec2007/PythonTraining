import datetime
a= datetime.datetime.now()
print a

x= a.day
y=a.hour

print x
print y

"""
by=lambda x: lambda y: getattr(y,x)
print by("x")
"""

print getattr (a,'day')