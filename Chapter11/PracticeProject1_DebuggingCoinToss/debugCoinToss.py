import random

guess = ''
# Make sure guess is either 'heads' or 'tails'
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

# Toss the coin: 0 for tails, 1 for heads
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# Map the guess to a number
if guess == 'heads':
    guess_num = 1
else:
    guess_num = 0

# First comparison
if toss == guess_num:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()  # Reuse `guess` for the second attempt

    # Map the new guess to a number
    if guess == 'heads':
        guess_num = 1
    else:
        guess_num = 0

    # Second comparison
    if toss == guess_num:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
