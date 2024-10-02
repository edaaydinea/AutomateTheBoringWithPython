import pyinputplus as pyip

# The limit argument specifies the number of attempts the user has to enter a valid value. If the user exceeds the number of attempts, pyinputplus will raise a RetryLimitException exception.

# The timeout argument specifies the number of seconds the user has to enter a valid value. If the user exceeds the number of seconds, pyinputplus will raise a TimeoutException exception.

# The default argument specifies the default value that pyinputplus will return if the user enters a blank value. If the user enters a blank value, pyinputplus will return the default value.
response = pyip.inputNum(limit=2)
print(response)

response = pyip.inputNum(limit=2, default='N/A')
print(response)

