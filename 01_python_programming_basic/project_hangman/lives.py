def set_lives(difficulty: str = "medium") -> int:
    if difficulty == "easy":
        lives = 7
    elif difficulty == "medium":
        lives = 5
    else:
        lives = 3
    return lives
