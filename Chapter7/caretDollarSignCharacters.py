import re

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo.group()) # Hello
print(beginsWithHello.search('He said hello.') == None) # True

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print(mo.group()) # 2
print(endsWithNumber.search('Your number is forty two.') == None) # True

wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print(mo.group()) # 1234567890
print(wholeStringIsNum.search('12345xyz67890') == None) # True
print(wholeStringIsNum.search('12 34567890') == None) # True