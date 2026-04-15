import random

choose = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

user_chose = int(
    input("what do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
)
computer_chose = random.randint(0, 2)
if user_chose > 2:
    print("Try again and Type 0 for Rock, 1 for Paper or 2 for Scissors")
else:
    print(choose[user_chose])
    print("\nComputer chose\n")
    print(choose[computer_chose])
    if user_chose == computer_chose:
        print("Draw")
    elif user_chose == 0 and computer_chose == 2:
        print("YOU WIN")
    elif user_chose == 2 and computer_chose == 1:
        print("YOU WIN")
    elif user_chose == 1 and computer_chose == 0:
        print("YOU WIN")
    else:
        print("COMPUTER WIN")
