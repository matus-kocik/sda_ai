from constants import HANGMAN


def get_hangman_pictures(lives: int, hangman_picture=HANGMAN) -> list[str]:
    if lives == 3:
        indices: list[int] = [1, 2, 5, 7]
    elif lives == 5:
        indices: list[int] = [0, 1, 2, 3, 5, 7]
    elif lives == 7:
        indices: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]
    else:
        return hangman_picture

    return [hangman_picture[i] for i in indices]
