import pyinputplus as pyip

while True:
    response = pyip.inputYesNo("Want to know how to keep an idiot busy for hours? ")
    
    if response == 'no':
        print("Thank you. Have a nice day.")
        break
