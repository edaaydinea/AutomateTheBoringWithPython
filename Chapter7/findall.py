import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall('Call me at 415-555-4242 or 415-555-4243')
print(mo) # ['415-555-4242', '415-555-4243']

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) # [('415', '555', '9999'), ('212', '555', '0000')]