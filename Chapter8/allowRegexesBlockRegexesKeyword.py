import pyinputplus as pyip

response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)

response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
print(response)

response = pyip.inputNum(blockRegexes=[r'[02468]$'])
print(response)

response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(response)