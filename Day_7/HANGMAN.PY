import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

n = 0
lives = 7
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
len_word = len(chosen_word)
display = []
for _ in chosen_word:
    display.append("_")
# print(display)
print(f"The random list is {chosen_word}")  # for test ...
while lives > 0 and "_" in display:
    guess = input("Guess a Letter: ").lower()
    n = 0
    for i in chosen_word:
        if guess == i:
            display[n] = guess
        n += 1
    if guess not in chosen_word:
        print(HANGMANPICS[7-lives])
        lives -= 1
    print(display)
if lives > 0 :
    print("YOU WIN!")
else:
    print("YOU LOSE!")
