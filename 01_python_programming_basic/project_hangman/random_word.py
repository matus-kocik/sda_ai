import random
from constants import DATA


def get_random_word(data=DATA) -> str:
    words: list = []
    with open(data) as f:
        file: list[str] = f.readlines()

    for line in file:
        country: str = line.strip().split(" | ")[0]
        words.append(country)

    word_to_guess: str = random.choice(words)
    return word_to_guess
