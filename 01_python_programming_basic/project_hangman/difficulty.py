import time


def get_difficulty():
    difficulty_settings = {
        "1": {"name": "easy", "lives": 7},
        "2": {"name": "medium", "lives": 5},
        "3": {"name": "hard", "lives": 3},
    }

    while True:
        player_difficulty = input(
            """👉 Please, select difficulty (1, 2, 3 or easy, medium, hard): 
            1. easy: 7 lives (for beginners)
            2. medium: 5 lives (balanced challenge)
            3. hard: 3 lives (only for the brave!)\n"""
        ).lower()

        if player_difficulty in difficulty_settings:
            chosen = difficulty_settings[player_difficulty]
            lives = chosen["lives"]
            time.sleep(1)
            break
        elif player_difficulty in ["easy", "medium", "hard"]:
            for key, value in difficulty_settings.items():
                if value["name"] == player_difficulty:
                    lives = value["lives"]
                    time.sleep(1)
                    break
            break
        else:
            print("Invalid choice. Please type 1, 2, 3 or 'easy', 'medium', 'hard'.")

    return lives
