import pyinputplus as pyip

# The blank argument specifies whether the user can enter a blank value. If the user enters a blank value, pyinputplus will keep asking the user for a value until the user enters a non-blank value.
response = pyip.inputNum('Enter a number: ', blank=False)
print(response)

