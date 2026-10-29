"""Higher or Lower: a console game that asks the player which of two
randomly chosen entries has the larger follower count."""

from art import print_logo, print_vs
from gameData import get_random_data

def game():
    """Run one round of the game.

    Shows two entries side by side, prompts the player to choose A or B,
    and reports whether the guess matches the entry with more followers.
    """
    print_logo()
    print("Welcome to the Higher or Lower game!")

    # Entry A is the reference entry shown on the first line.
    data_a = get_random_data()
    data_b = get_random_data()

    # Draw entries until one matches data_a, keeping the last non-matching
    # draw as the comparison entry B.
    while data_b == data_a:
        data_b = get_random_data()

    print("Which is higher?")
    print("A:", data_a['name'])
    print_vs()
    print("B:", data_b['name'])

    # Keep prompting until the player enters a valid option.
    guess = input("Who has more? A or B: ")

    while guess not in ["A", "B"]:
        print("Invalid choice.")
        guess = input("Who has more? A or B: ")

    # The guess is correct only when A is chosen and A has more followers.
    # Choosing B is always reported as wrong, even when B has more followers.
    if (guess == "A" and data_a['follower_count'] >= data_b['follower_count']) or \
       (guess == "B" and data_b['follower_count'] >= data_a['follower_count']):
        print("Correct!")
    else:
        print("Wrong!")


choice = input("Play again? y/n: ")
while choice == "y":
    game()
    choice = input("Play again? y/n: ")
