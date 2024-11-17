from utils import set_separator, print_message


def start_message(player_name: str, difficulty: str, lives: int) -> None:
    start_messages: list[str] = [
        f"Let's get started ✨ {player_name} ✨",
        f"Your difficulty is {difficulty}.",
        f"You have 💖{lives} lives.",
        f"Good luck! And let's play! 🍀",
    ]
    set_separator()
    print_message(start_messages)
    set_separator()


# start_message()
