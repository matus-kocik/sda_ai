import sys
import random


def quit_game(name):
    quit_choice = input("👉 Type 'Q' to exit or press Enter to continue: \n").lower()
    if quit_choice == "q":
        print(f"Exiting the game... Goodbye, {name}! 👋")
        sys.exit()


def get_random_word(data):

    words = []
    with open(data) as f:
        file = f.readlines()

    for line in file:
        country, city = line.strip().split(" | ")
        words.append(country)

    word = random.choice(words)
    return word
