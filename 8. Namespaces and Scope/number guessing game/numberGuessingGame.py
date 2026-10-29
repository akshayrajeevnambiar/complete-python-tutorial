from art import display_logo
from random import randint

display_logo()

def get_random_number():
    return randint(1, 100)

def check_guess(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True

def start_game():
    print("Im thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    answer = get_random_number()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if check_guess(guess, answer):
            print("Congratulations! You guessed the number correctly.")
            return
        attempts -= 1
    print(f"You've run out of attempts. The number was {answer}.")

start_game()