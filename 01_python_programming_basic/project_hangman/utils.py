import sys
import time


def set_game_time_sleep() -> None:
    time.sleep(1)


def set_separator(sep: str = "*"):
    print(100 * sep)


def quit_game(player_name: str = "Anonym") -> None:
    quit_choice: str = input(
        "👉 Type 'Q' to exit or press Enter to continue: \n"
    ).lower()
    if quit_choice == "q":
        print(f"Exiting the game... Goodbye, {player_name}! 👋")
        sys.exit()


def print_message(messages) -> None:
    for message in messages:
        print()
        print(message)
        set_game_time_sleep()
