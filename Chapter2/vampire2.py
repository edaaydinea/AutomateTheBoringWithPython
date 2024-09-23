name = "Carol"
age = 3000

if name == "Alice":
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.")
elif age >100:
    print("You are not Alice, grannie.")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
    
# You might expect the code to print the string "Unlike you, Alice is not an undead, immortal vampire." However, because the age > 100 condition is True (after all 3000 is greater than 100), the string "You are not Alice, grannie." is printed instead. The code will never reach the age > 2000 condition because the age > 100 condition is True first.
    