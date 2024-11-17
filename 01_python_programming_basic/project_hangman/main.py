from difficulty import get_difficulty
from game import game
from hangman_picture import get_hangman_pictures
from lives import set_lives
from player_name import get_player_name
from random_word import get_random_word
from welcome_message import welcome_message
from start_message import start_message


def main():

    welcome_message()

    player_name: str = get_player_name()
    difficulty: str = get_difficulty()
    lives: int = set_lives(difficulty)
    word_to_guess: str = get_random_word()
    hangman_picture: list[str] = get_hangman_pictures(lives)

    start_message(player_name, difficulty, lives)

    game(word_to_guess, hangman_picture, lives)


if __name__ == "__main__":
    main()
