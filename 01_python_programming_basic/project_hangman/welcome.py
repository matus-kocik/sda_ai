import time


def print_message(messages):
    for message in messages:
        print(message)
        time.sleep(1)


def first_welcome_message():
    first_welcome_messages = [
        "",
        "🟢 Welcome to HANGMAN by Koco! 🟢",
        "",
        "🌍 In this version, the word is a country or its capital.",
        "🎯 Your goal is to guess the hidden word by guessing letters.",
        "❗ But beware!!! If you make too many mistakes, the game is over.",
        "",
    ]
    print_message(first_welcome_messages)


def get_player_name():
    name = input("👉 Please, enter your name:\n")
    return name


def second_welcome_message(name, lives):
    second_welcome_messages = [
        "",
        f"Let's get started {name}",
        f"You have {lives} lives.",
        "Good luck! 🍀",
        "",
    ]
    print_message(second_welcome_messages)
