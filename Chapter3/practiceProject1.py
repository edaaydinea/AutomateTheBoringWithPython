def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
        
    print(result)
    return result

try:
    number = int(input("Enter a number: "))
    while number != 1:
        number = collatz(number)
except ValueError:
    print("Please enter an integer.")