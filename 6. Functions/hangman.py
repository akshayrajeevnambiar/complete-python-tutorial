from hangmanWordsList import get_random_word
from hangmanArt import logo, stages

WORD = get_random_word()


def get_user_choice() -> str:
    return input("Enter the letter choice here : ")


def generate_blank_spaces(word: str) -> str:
    word_list = list(word)
    return ["_"] * len(word_list)


def print_logo() -> None:
    print(logo)


def game_logic(word_list: list, display_list: list, letter: str, lives: int):
    if letter in word_list:
        for i in range(len(word_list)):
            if letter == word_list[i]:
                display_list[i] = word_list[i]
    else:
        lives -= 1
        print(stages[lives])
        print(f"You guessed '{letter}', that's not in the word. You lose a life.")
    return display_list, lives


def game():
    game_condition = True
    lives = len(stages)
    display = generate_blank_spaces(WORD)

    while lives > 0 and game_condition:
        print(''.join(display))
        letter = get_user_choice()
        display, lives = game_logic(list(WORD), list(display), letter, lives)

        if "_" not in display:
            print(f"You guessed it, '{''.join(display)}' was the correct answer.")
            game_condition = False

    if lives == 0:
        print(f"You lost, the correct word was '{WORD}'.")

print_logo()
game()
