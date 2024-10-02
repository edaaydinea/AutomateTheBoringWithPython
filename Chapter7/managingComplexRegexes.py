import re

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4} (\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

mo = phoneRegex.search('Call me at 415-555-4242 ext. 12345')
print(mo.group()) # 415-555-4242 ext. 12345
mo = phoneRegex.search('Call me at (415) 555-4242')
print(mo.group()) # (415) 555-4242
mo = phoneRegex.search('Call me at 415.555.4242')
print(mo.group()) # 415.555.4242
mo = phoneRegex.search('Call me at 415 555 4242')
print(mo.group()) # 415 555 4242
mo = phoneRegex.search('Call me at 415-555-4242')
print(mo.group()) # 415-555-4242
mo = phoneRegex.search('Call me at 555-4242')
print(mo.group()) # 555-4242