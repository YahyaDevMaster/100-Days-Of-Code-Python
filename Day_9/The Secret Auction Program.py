import os
import logo

bidders = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bidders_log(names, bids):
    bidders[names] = bids


turnon = True
logo
while turnon:
    print("Welcome to the secret auction program")
    name = input("what is your name ?: ")
    bid = int(input("What's your bid?: $"))
    bidders_log(name, bid)
    other = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if other == "no":
        turnon = False
    clear()

winner_bid = 0
winner_name=""
for key, value in bidders.items():
    if winner_bid < value:
        winner_bid = value
        winner_name = key


print(f"The winner is {winner_name}")
