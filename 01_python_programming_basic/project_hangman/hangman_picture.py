

from constants import HANGMAN


def get_hangman_pictures(lives: int = 5, hangman_picture=HANGMAN) -> list[str]:
    if lives == 3:
        indices: list[int] = [0, 2, 4, 6]
    elif lives == 5:
        indices: list[int] = [0, 1, 2, 3, 4, 6]
    else:
        return hangman_picture
    return [hangman_picture[i] for i in indices]
