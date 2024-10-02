import re

def isPhoneNumber(text):
    # %d is a digit character, {3} means 3 times
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search(text)
    if mo is None:
        return False
    return True

print("Is 415-555-4242 a phone number?")
print(isPhoneNumber('415-555-4242'))
print("Is Moshi moshi a phone number?")
print(isPhoneNumber('Moshi moshi'))