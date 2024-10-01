import zombiedice
import random

class RandomDecisionZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # First roll
        if diceRollResults is not None:
            if random.choice([True, False]):
                zombiedice.roll()  # Randomly decide to roll again

class TwoBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        diceRollResults = zombiedice.roll()  # First roll

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains >= 2:
                break  # Stop after two brains
            diceRollResults = zombiedice.roll()  # Roll again

class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll()  # First roll

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break  # Stop after two shotguns
            diceRollResults = zombiedice.roll()  # Roll again

class RandomRollsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        rolls = random.randint(1, 4)  # Decide to roll 1 to 4 times
        diceRollResults = zombiedice.roll()  # First roll

        while diceRollResults is not None and rolls > 0:
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break  # Stop if two shotguns
            rolls -= 1
            diceRollResults = zombiedice.roll()  # Roll again

class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        brains = 0
        diceRollResults = zombiedice.roll()  # First roll

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns > brains:
                break  # Stop if shotguns exceed brains
            diceRollResults = zombiedice.roll()  # Roll again

zombies = (
    RandomDecisionZombie(name='Random Decision'),
    TwoBrainsZombie(name='Two Brains'),
    TwoShotgunsZombie(name='Two Shotguns'),
    RandomRollsZombie(name='Random Rolls'),
    MoreShotgunsThanBrainsZombie(name='More Shotguns Than Brains'),
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
