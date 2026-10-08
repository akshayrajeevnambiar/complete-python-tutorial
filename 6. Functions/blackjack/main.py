# BLACKJACK CLI PROJECT TODO LIST

from art import print_logo
from cards import get_random_card

PLAYER_HAND = []
DEALER_HAND = []

def draw_card (hand: list, times = 1):
    for _ in range(times):  
        hand.append(get_random_card())

def display_cards (player: str, hand:list):
    if player == "Dealer":
        print(f"{player} {' '.join([card for card in hand[:-1]])} ? | Score : {calculate_hand_value(hand[:-1])}")
    else:
        print(f"{player} : {" ".join([card for card in hand])} | Score : {calculate_hand_value(hand)}")

# --- 3. HAND VALUE ---

def calculate_hand_value(hand: list) -> int:
    value = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            value += 10
        elif card == "A":
            value += 11
            aces += 1   
        else:
            value += int(card)
    
    while aces > 0 and value > 21:
        value -= 10
        aces -= 1
    
    return value


# --- 4. PLAYER'S TURN ---
def player_turn():
    player_hand_value = calculate_hand_value(PLAYER_HAND)

    while calculate_hand_value(PLAYER_HAND) < 21:
        choice = input("Hit or Stand : ").lower().strip()
        if choice == "hit":
            draw_card(PLAYER_HAND) 
            display_cards("Player", PLAYER_HAND)
        elif choice == "stand":
            break
        else:
            print("Choice not supported! Please try again....")

    if calculate_hand_value(PLAYER_HAND) > 21:
        print("Busted!!")
    else:
        print(f"Player stands with a score of {player_hand_value}")
        dealer_turn()

def dealer_turn():
    
    while calculate_hand_value(DEALER_HAND) < 21:
        if calculate_hand_value(DEALER_HAND) < 17:
            draw_card(DEALER_HAND)
            display_cards("Dealer ", DEALER_HAND)
        else:
            print(f"Dealer stands with a score of {calculate_hand_value(DEALER_HAND)}")
            break
    if calculate_hand_value(DEALER_HAND) > 21:
        print("Dealer busts!!")

def game_result():
    player_score = calculate_hand_value(PLAYER_HAND)
    dealer_score = calculate_hand_value(DEALER_HAND)

    if player_score > dealer_score:
        print("Player wins!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

def game():
    print_logo()
    draw_card(PLAYER_HAND, 2)
    draw_card(DEALER_HAND, 2)
    display_cards("Player", PLAYER_HAND)
    display_cards("Dealer", DEALER_HAND)

    player_turn()
    game_result()

game()
