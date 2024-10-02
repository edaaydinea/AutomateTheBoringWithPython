"""
Write a function that takes a string and does the same thing as the strip() string method. If no other
arguments are passed other than the string to strip, then whitespace characters will be removed from the
beginning and end of the string. Otherwise, the characters specified in the second argument to the function
will be removed from the string.
"""

import re

def strip(text, chars=None):
    if chars is None:
        stripRegex = re.compile(r'^\s*|\s*$')
    else:
        stripRegex = re.compile(r'^[' + chars + ']*|[' + chars + ']*$')
    return stripRegex.sub('', text)

print(strip('    Hello, World!    '))
print(strip('    Hello, World!    ', 'Helo'))
print(strip('    Hello, World!    ', 'Helo '))
print(strip('    Hello, World!    ', 'Helo W'))
print(strip('    Hello, World!    ', 'Helo W!'))
