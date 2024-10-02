import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group()) # Batwoman

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group()) # Batwowowowoman

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None) # True