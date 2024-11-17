import random
from typing import LiteralString
from difficulty import get_difficulty
from hangman_picture import get_hangman_pictures
from lives import set_lives
from player_name import get_player_name
from random_word import get_random_word
from constants import question_pool_letter


def game(
    word_to_guess,
    hangman_picture,
    difficulty="hard",
    lives=3,
    player_name="Matus",
):
    guess = 0
    already_tried_letters = set()
    hidden_word: list[str] = ["_" for i in word_to_guess]
    remaining_lives: int = lives

    while "_" in hidden_word and remaining_lives > 0:
        print(f"\nWord to guess: {" ".join(hidden_word)}")
        print(f"Tried letters: {", ".join(sorted(already_tried_letters))}")
        print(f"Remaining lives: {remaining_lives}")
        print(hangman_picture[lives - remaining_lives])

        question: str = random.choice(question_pool_letter)
        guess_letter: str = input(question).strip().lower()

        if not guess_letter.isalpha() or len(guess_letter) != 1:
            print("Please enter a valid letter.")
            continue

        if guess_letter in already_tried_letters:
            print(f"You've already tried the letter '{guess_letter}'. Try another one.")
        else:
            already_tried_letters.add(guess_letter)

        if guess_letter in word_to_guess:
            print(f"Good job! The letter '{guess_letter}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess_letter:
                    hidden_word[i] = guess_letter
        else:
            print(f"Sorry, the letter '{guess_letter}' is not in the word.")
            remaining_lives -= 1

    if "_" not in hidden_word:
        print("\n 🎉 Congratulations! You've guessed the word:", "".join(hidden_word))
    else:
        print("\n 💀 Game Over! The word was:", word_to_guess)

# player_name: str = get_player_name()
# difficulty: str = get_difficulty()
# lives: int = set_lives(difficulty)
word_to_guess: str = get_random_word()
hangman_picture: list[str] = get_hangman_pictures(lives=3)

game(word_to_guess, hangman_picture)
