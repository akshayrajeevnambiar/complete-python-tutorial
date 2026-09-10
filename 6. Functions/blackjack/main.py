# BLACKJACK CLI PROJECT TODO LIST

from art import print_logo
from cards import get_random_card

player_hand = []
dealer_hand = []

def draw_card (hand: list, times = 1):
    for _ in range(times):  
        hand.append(get_random_card())

def display_cards (name: str, hand:list):
    print(f"{name} : {" ".join([card for card in hand])}")

# --- 3. HAND VALUE ---
# TODO: Create a function that calculates the value of a hand

def calculate_hand_value(hand: list) -> int:
    value = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            value += 10
        elif card == "A":
            value += 11
        else:
            value += int(card)

    
# TODO: Count Jack, Queen, and King as 10
# TODO: Count an Ace as 11 when possible
# TODO: Change an Ace from 11 to 1 if the hand would otherwise go over 21

# --- 4. PLAYER'S TURN ---
# TODO: Ask the player to choose "hit" or "stand"
# TODO: Deal another card when the player chooses "hit"
# TODO: Display the player's updated hand and score
# TODO: Keep asking until the player stands or goes over 21
# TODO: End the round if the player busts

# --- 5. DEALER'S TURN ---
# TODO: Reveal the dealer's hidden card
# TODO: Make the dealer hit while their score is below 17
# TODO: Make the dealer stand when their score is 17 or higher
# TODO: End the round if the dealer busts

# --- 6. DETERMINE THE WINNER ---
# TODO: Check whether the player has a natural Blackjack
# TODO: Check whether the dealer has a natural Blackjack
# TODO: Declare the dealer as the winner if the player busts
# TODO: Declare the player as the winner if the dealer busts
# TODO: Compare scores when neither player busts
# TODO: Handle a tie, also called a push
# TODO: Display the result clearly

# --- 7. GAME LOOP ---
# TODO: Ask the player if they want to play another round
# TODO: Create and shuffle a fresh deck for the next game
# TODO: Reset both hands before starting the next round
# TODO: Exit the program cleanly when the player chooses to stop

# --- 8. INPUT VALIDATION ---
# TODO: Handle uppercase and lowercase input
# TODO: Reject invalid hit-or-stand choices
# TODO: Keep asking until the player enters a valid choice
# TODO: Reject invalid play-again choices

# --- 9. CODE ORGANIZATION ---
# TODO: Separate the game into small functions
# TODO: Create a function for building the deck
# TODO: Create a function for dealing a card
# TODO: Create a function for calculating a hand's value
# TODO: Create a function for displaying cards
# TODO: Create a function for the player's turn
# TODO: Create a function for the dealer's turn
# TODO: Create a function for determining the winner
# TODO: Create a main function that controls the complete game

# --- 10. TESTING ---
# TODO: Test a normal player win
# TODO: Test a normal dealer win
# TODO: Test a tie
# TODO: Test a player bust
# TODO: Test a dealer bust
# TODO: Test a Blackjack
# TODO: Test a hand containing one Ace
# TODO: Test a hand containing multiple Aces
# TODO: Test invalid user input

# --- OPTIONAL IMPROVEMENTS ---
# TODO: Track the number of player wins, dealer wins, and ties
# TODO: Add a starting chip balance
# TODO: Allow the player to place bets
# TODO: Add double-down functionality
# TODO: Add card-splitting functionality
# TODO: Use classes to represent Card, Deck, Hand, and Player
# TODO: Add ASCII-art cards
# TODO: Save game statistics to a file