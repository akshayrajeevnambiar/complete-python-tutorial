# TODO-1: Ask the user for input
def get_user_bid() -> list:
    name = input("please enter your name : ")
    bid = float(input("please enter your bid amount: "))
    return name, bid

def check_next_condition ():
    choice = input("Would someone else like to add thier bid (y/n)")
    return True if choice.lower() == 'y' else False

# TODO-2: Save data into dictionary {name: price}
def save_user_bids(user_bids: dict):
    flag = True
    while flag:
        clear_screen()
        name, bid = get_user_bid()
        user_bids[name] = bid

        flag = check_next_condition()

def check_auction_winner(user_bids: dict):
    return max(user_bids.values())

def clear_screen():
    print("\033c", end="")

user_bids = dict()
save_user_bids(user_bids)
print(check_auction_winner(user_bids))
