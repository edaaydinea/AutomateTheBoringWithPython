import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) # Batwoman

phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group()) # 415-555-4242

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group()) # 555-4242