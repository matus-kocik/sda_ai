DATA = "countries-and-capitals.txt"

HANGMAN: list[str] = [
    """
  +---+
      |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

question_pool_letter: list[str] = [
    "Guess a letter: \n",
    "Enter a letter to guess: \n",
    "Which letter do you choose? \n",
    "Take a guess! What letter might be in the word? \n",
    "The word awaits! Which letter do you think is hiding in it? \n",
    "Brave guesser, pick a letter to reveal your fate! \n",
    "Can you uncover a piece of the puzzle? Guess a letter: \n",
    "Which letter do you think will crack the code? \n",
]
