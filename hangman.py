import random

# Hangman stages for incorrect guesses
HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

# Word list for the game
WORDS = [
    "PYTHON",
    "COMPUTER",
    "PROGRAM",
    "DEVELOPER",
    "KEYBOARD",
    "DATABASE",
    "INTERNET",
    "SOFTWARE"
]


def display_game(secret_word, guessed_letters, wrong_guesses):
    """Display the current game status."""
    print(HANGMAN_STAGES[wrong_guesses])

    masked_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:", masked_word)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print(f"Wrong attempts: {wrong_guesses}/6")


def get_guess(guessed_letters):
    """Get and validate a single-letter guess."""
    while True:
        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter one English letter (A-Z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. No penalty!")
            continue

        return guess


def play_game():
    """Run one complete Hangman game."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 40)
    print("       HANGMAN WORD GUESSING GAME")
    print("=" * 40)
    print("Guess the hidden word, one letter at a time!")
    print("You have 6 incorrect attempts.")

    while wrong_guesses < 6:
        display_game(secret_word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            break

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Incorrect guess!")

    display_game(secret_word, guessed_letters, wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("CONGRATULATIONS! You guessed the word!")
    else:
        print("GAME OVER! The correct word was:", secret_word)


def main():
    """Start the game and handle replay."""
    while True:
        play_game()

        replay = input("\nPlay again? (Y/N): ").strip().upper()

        if replay != "Y":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()