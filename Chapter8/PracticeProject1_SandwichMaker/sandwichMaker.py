import pyinputplus as pyip

# Define prices for each option
prices = {
    'wheat': 1.5,
    'white': 1.0,
    'sourdough': 1.75,
    'chicken': 2.5,
    'turkey': 2.75,
    'ham': 2.25,
    'tofu': 2.0,
    'cheddar': 1.0,
    'Swiss': 1.25,
    'mozzarella': 1.5,
    'mayo': 0.25,
    'mustard': 0.25,
    'lettuce': 0.5,
    'tomato': 0.5
}

# Ask user for their sandwich preferences
print("Let's make your sandwich!\n")

# Ask for bread type
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Choose a bread type:\n", numbered=True)

# Ask for protein type
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Choose a protein type:\n", numbered=True)

# Ask if user wants cheese
want_cheese = pyip.inputYesNo("Do you want cheese? (yes/no)\n")

cheese = ''
if want_cheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt="Choose a cheese type:\n", numbered=True)

# Ask if user wants mayo, mustard, lettuce, or tomato
want_mayo = pyip.inputYesNo("Do you want mayo? (yes/no)\n")
want_mustard = pyip.inputYesNo("Do you want mustard? (yes/no)\n")
want_lettuce = pyip.inputYesNo("Do you want lettuce? (yes/no)\n")
want_tomato = pyip.inputYesNo("Do you want tomato? (yes/no)\n")

# Ask how many sandwiches
num_sandwiches = pyip.inputInt("How many sandwiches would you like? ", min=1)

# Calculate total cost
total_cost = prices[bread] + prices[protein]

if want_cheese == 'yes':
    total_cost += prices[cheese]
if want_mayo == 'yes':
    total_cost += prices['mayo']
if want_mustard == 'yes':
    total_cost += prices['mustard']
if want_lettuce == 'yes':
    total_cost += prices['lettuce']
if want_tomato == 'yes':
    total_cost += prices['tomato']

# Multiply by the number of sandwiches
total_cost *= num_sandwiches

# Display total cost
print(f"\nThe total cost for your sandwich(es) is: ${total_cost:.2f}")
