import pyinputplus as pyip

# The min argument specifies the minimum value the user must enter. If the user enters a number less than the minimum, pyinputplus will keep asking the user for a number until the user enters a number that is greater than or equal to the minimum.
response = pyip.inputNum('Enter a number greater than 4: ', min=4)
print(response)

# The max argument specifies the maximum value the user must enter. If the user enters a number greater than the maximum, pyinputplus will keep asking the user for a number until the user enters a number that is less than or equal to the maximum.
response = pyip.inputNum('Enter a number less than 6: ', max=6)
print(response)

# The greaterThan argument specifies the minimum value the user must enter. If the user enters a number less than the minimum, pyinputplus will keep asking the user for a number until the user enters a number that is greater than the minimum.
response = pyip.inputNum('Enter a number greater than 4: ', greaterThan=4)
print(response)

# The lessThan argument specifies the maximum value the user must enter. If the user enters a number greater than the maximum, pyinputplus will keep asking the user for a number until the user enters a number that is less than the maximum.
response = pyip.inputNum('Enter a number less than 6: ', lessThan=6)
print(response)
