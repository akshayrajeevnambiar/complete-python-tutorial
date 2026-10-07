import os

bids = {}

choice = "yes"

while choice != "no":
    os.system("clear||cls")
    bidder_name = input("Whats your name: ")
    bid_amount = int(input("Whats your bid: "))

    bids[bidder_name] = bid_amount

    choice = input("Are there anymore bidders(yes/no): ").lower()

os.system("clear||cls")

winner_bid = 0
winner_name = ""
for key, value in bids.items():
    if value > winner_bid:
        winner_bid = value
        winner_name = key

print(f"Winner {winner_name} for the amount of ${winner_bid}")
