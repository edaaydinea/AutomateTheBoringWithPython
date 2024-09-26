import random

def coin_flip_streak_experiment():
    numberOfStreaks = 0
    total_experiments = 10000

    for experimentNumber in range(total_experiments):
        # Create a list of 100 randomly selected 'heads' (H) or 'tails' (T)
        flips = []
        for i in range(100):
            if random.randint(0, 1) == 0:
                flips.append('T')  # Tail
            else:
                flips.append('H')  # Head

        # Check for streaks of 6 heads or 6 tails in a row
        streak_count = 1  # To count consecutive occurrences of the same flip
        for j in range(1, len(flips)):
            if flips[j] == flips[j - 1]:
                streak_count += 1
                if streak_count == 6:  # Found a streak of 6
                    numberOfStreaks += 1
                    break  # No need to check further in this list
            else:
                streak_count = 1  # Reset streak count

    # Calculate the percentage of experiments with a streak
    chance_of_streak = (numberOfStreaks / total_experiments) * 100
    print(f'Chance of streak: {chance_of_streak:.2f}%')

# Run the experiment
coin_flip_streak_experiment()
