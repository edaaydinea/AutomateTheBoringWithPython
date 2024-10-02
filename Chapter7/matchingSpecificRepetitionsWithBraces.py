import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group()) # HaHaHa

mo2 = haRegex.search('Ha')
print(mo2 == None) # True