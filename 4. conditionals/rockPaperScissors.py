import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
         _______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Rock, Paper, Scissors: Type 0 for rock, 1 for paper, 2 for scissors.\n"))
game_hand_signs = [rock, paper, scissors]

computer_choice = random.randint(0, len(game_hand_signs) - 1)

print("Computers Choice \n", game_hand_signs[computer_choice])
print("Player Choice \n", game_hand_signs[player_choice])

if player_choice == computer_choice:
    print("Draw!")

elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print("You Win!")

else:
    print("You Lose!")
