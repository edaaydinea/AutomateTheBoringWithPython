def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
        
    print(result)
    return result

while True:
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Please enter a positive integer.")
        else:
            break 
    except ValueError:
        print("Invalid output. Please enter an integer.")
    # negative numbers are not allowed, otherwise the program will run indefinitely

while number != 1:
    number = collatz(number)