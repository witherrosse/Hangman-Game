# Word list separated for scalability / easy modification
WORD_LIST = [
    "python", "hangman", "challenge", "developer", "programming",
    "treasure", "island", "password", "quiz", "snake"
]

import random
from words import WORD_LIST

MAX_ATTEMPTS = 6

def choose_word():
    """Randomly select a word from WORD_LIST."""
    return random.choice(WORD_LIST).lower()

def display_word(word, guessed_letters):
    """Return the current progress of the word with underscores for missing letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main Hangman game loop."""
    word = choose_word()
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("🪢 Welcome to Hangman!")
    print(f"You have {attempts_left} attempts to guess the word.")
    print(display_word(word, guessed_letters))

    while attempts_left > 0 and set(word) != guessed_letters:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            attempts_left -= 1
            print(f"❌ Wrong! Attempts left: {attempts_left}")

        print(display_word(word, guessed_letters))
        print()

    if set(word) == guessed_letters:
        print(f"🏆 Congratulations! You guessed the word: {word}")
    else:
        print(f"💀 Game Over! The word was: {word}")


if __name__ == "__main__":
    hangman()


