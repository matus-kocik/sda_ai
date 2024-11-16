import time
from difficulty import get_difficulty
from welcome import first_welcome_message, second_welcome_message, get_player_name
from utils import quit_game


def main():
    first_welcome_message()

    name = get_player_name()
    time.sleep(1)

    quit_game(name)
    time.sleep(1)

    lives = get_difficulty()
    time.sleep(1)

    quit_game(name)
    time.sleep(1)

    second_welcome_message(name, lives)
    time.sleep(1)

    quit_game(name)
    time.sleep(1)

if __name__ == "__main__":
    main()
