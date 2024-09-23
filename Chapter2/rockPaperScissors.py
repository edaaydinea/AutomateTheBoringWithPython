import random, sys
print('ROCK, PAPER, SCISSORS')
# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')
        
    # Display the player's move:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
        
    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
        
    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif (playerMove == 'r' and computerMove == 's') or (playerMove == 's' and computerMove == 'p') or (playerMove == 'p' and computerMove == 'r'):
        print('You win!')
        wins = wins + 1
    elif (playerMove == 'r' and computerMove == 'p') or (playerMove == 's' and computerMove == 'r') or (playerMove == 'p' and computerMove == 's'):
        print('You lose!')
        losses = losses + 1
        
# The code will keep track of the number of wins, losses, and ties the player has. The outer while loop will keep looping forever, so the player can play multiple games of rock, paper, scissors. The inner while loop will keep asking the player to enter their move until the player types 'r', 'p', 's', or 'q'. If the player types 'q', the sys.exit() function call will terminate the program. If the player types 'r', 'p', or 's', the inner while loop will break, and the player's move will be displayed. The computer's move will be randomly chosen and displayed. The win/loss/tie result will be displayed, and the number of wins, losses, and ties will be updated. The player can then play another round of rock, paper, scissors.