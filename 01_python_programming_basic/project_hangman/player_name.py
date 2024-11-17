from utils import set_game_time_sleep


def get_player_name() -> str:
    print()
    player_name: str = input("👉 Please, enter your name:\n").capitalize()
    set_game_time_sleep()
    return player_name
