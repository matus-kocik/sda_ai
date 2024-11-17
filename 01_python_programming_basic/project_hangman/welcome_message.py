from utils import print_message, set_separator


def welcome_message() -> None:
    welcome_messages: list[str] = [
        "🌟 Welcome to the Ultimate HANGMAN Challenge! 🌟",
        "🌍 This time, it's all about geography – the hidden word is the name of a country.",
        "🔍 Test your knowledge and guessing skills as you unveil the mystery, letter by letter.",
        "🚨 Careful! Each wrong guess brings you closer to defeat. Outsmart the hangman if you can!",
    ]
    set_separator()
    print_message(welcome_messages)
    set_separator()


# welcome_message()
