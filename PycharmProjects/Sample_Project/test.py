"""
import pandas

df = pandas.DataFrame({"A": [11, 12, 13], "B": [34, 78, 109]})

print df

file = open('keywords.txt', 'r')
print file.read()
for line in file:
    print line.split('|')[0]
"""

with open('keywords.txt') as file:
    keyword = [line.split('|')[0] for line in file]
print keyword