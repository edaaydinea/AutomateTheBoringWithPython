# Import the regex module with import re and call re.compile() to create a regex object.
# Pass the string you want to search into the regex object’s search() method. This returns a Match object.
# Call the Match object’s group() method to return the matched string.

import re

def isPhoneNumber(text):
    # turkish phone number regex
    # +90 555 555 55 55
    phoneNumRegex = re.compile(r'\+\d{2} \d{3} \d{3} \d{2} \d{2}')
    mo = phoneNumRegex.search(text)
    if mo is None:
        return False
    return True

print("Is +90 555 555 55 55 a phone number?")
print(isPhoneNumber('+90 555 555 55 55'))
print("Is Moshi moshi a phone number?")
print(isPhoneNumber('Moshi moshi'))