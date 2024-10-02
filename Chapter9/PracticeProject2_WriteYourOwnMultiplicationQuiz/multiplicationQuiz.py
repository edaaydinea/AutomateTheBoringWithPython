import random
import time

# Function to check the user's answer
def check_answer(question, correct_answer, max_attempts=3, time_limit=8):
    attempts = 0
    start_time = time.time()  # Record the start time

    while attempts < max_attempts:
        try:
            # Check if the time limit has passed
            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                print("Time's up! Moving on to the next question.")
                return False

            # Get the user's answer
            answer = int(input(f"{question}: "))

            # Check if the answer is correct
            if answer == correct_answer:
                print("Correct!")
                return True
            else:
                print("Incorrect.")
                attempts += 1

        except ValueError:
            # Handle non-integer inputs
            print("Please enter a valid number.")
            attempts += 1

    print(f"Out of attempts! The correct answer was {correct_answer}.")
    return False

# Quiz setup
def multiplication_quiz(num_questions=10):
    score = 0

    for i in range(num_questions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        correct_answer = num1 * num2
        question = f"What is {num1} x {num2}"

        # Ask the question and check the answer
        if check_answer(question, correct_answer):
            score += 1

        # Pause for 1 second between questions
        time.sleep(1)

    print(f"\nYour final score is: {score}/{num_questions}")

# Run the quiz
multiplication_quiz()
