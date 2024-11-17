def get_difficulty() -> str:
    

    player_difficulty: str = input(
        """👉 Please, select difficulty (1, 2, 3 or easy, medium, hard): 
            1. easy: 7 lives (for beginners)
            2. medium: 5 lives (balanced challenge)
            3. hard: 3 lives (only for the brave!)\n"""
    ).lower()

    if player_difficulty in ["easy", "1"]:
        difficulty = "easy"
    elif player_difficulty in ["medium", "2"]:
        difficulty = "medium"
    else:
        difficulty = "hard"

    return difficulty
