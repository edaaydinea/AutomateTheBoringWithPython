"""
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
password is defined as one that is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string against multiple regex patterns to
validate its strength.
"""

import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    digitRegex = re.compile(r'\d')
    if digitRegex.search(password) is None:
        return False
    lowercaseRegex = re.compile(r'[a-z]')
    if lowercaseRegex.search(password) is None:
        return False
    uppercaseRegex = re.compile(r'[A-Z]')
    if uppercaseRegex.search(password) is None:
        return False
    return True

print("Is '12345678' a strong password?")
print(is_strong_password('12345678'))
print("Is '12345678a' a strong password?")
print(is_strong_password('12345678a'))
print("Is '12345678A' a strong password?")
print(is_strong_password('12345678A'))
print("Is '12345678Aa' a strong password?")
print(is_strong_password('12345678Aa'))
print("Is '12345678Aa!' a strong password?")
print(is_strong_password('12345678Aa!'))