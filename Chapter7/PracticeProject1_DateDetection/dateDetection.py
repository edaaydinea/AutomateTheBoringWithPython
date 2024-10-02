"""
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range
from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day
or month is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept
nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April, June, September, and November
have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap
years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year
is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized
regular expression that can detect a valid date.
"""


import re

dateRegex = re.compile(r'((0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/([1-2][0-9]{3}))')

def is_valid_date(date):
    date = date.split('/')
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    if month in [4, 6, 9, 11] and day > 30:
        return False
    elif month == 2:
        if day > 29:
            return False
        elif day == 29 and year % 4 != 0:
            return False
        elif day == 29 and year % 100 == 0 and year % 400 != 0:
            return False
    return True

print("Is 31/02/2020 a valid date?")
print(is_valid_date('31/02/2020'))
print("Is 29/02/2020 a valid date?")
print(is_valid_date('29/02/2020'))
print("Is 29/02/2021 a valid date?")
print(is_valid_date('29/02/2021'))
print("Is 31/04/2021 a valid date?")
print(is_valid_date('31/04/2021'))
print("Is 31/05/2021 a valid date?")
print(is_valid_date('31/05/2021'))