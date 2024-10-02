import pyinputplus as pyip

# The inputStr() function checks that the user entered a string value. If the user enters a non-string value, the function will keep asking the user for a string value until the user enters a valid value.
response = pyip.inputNum(prompt='Enter a number: ')
print(response)

# The inputInt() function checks that the user entered a integer value. If the user enters a non-integer value, the function will keep asking the user for a integer value until the user enters a valid value.
response = pyip.inputInt(prompt='Enter a integer number: ')
print(response)

# The inputFloat() function checks that the user entered a float value. If the user enters a non-float value, the function will keep asking the user for a float value until the user enters a valid value.
response = pyip.inputFloat(prompt='Enter a float number: ')
print(response)
