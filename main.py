from replit import clear
import random
import hangman_words
from hangman_art import logo, stages

def choose_word():
    return random.choice(hangman_words.word_list)

def display_word(chosen_word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in chosen_word])

def hangman():
    chosen_word = choose_word()
    word_length = len(chosen_word)
    lives = 6
    guesses = []

    print(logo)

    while lives > 0:
        guess = get_guess(guesses)
        clear()

        if guess in guesses:
            print(f"You've already guessed {guess}")

        if guess in chosen_word:
            guesses.append(guess)
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

        current_display = display_word(chosen_word, guesses)
        print(current_display)

        if '_' not in current_display:
            print("You win!")
            return

        print(stages[lives])

    print(f"You lose. The word was {chosen_word}")

def get_guess(previous_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1 and guess not in previous_guesses:
            return guess
        elif guess in previous_guesses:
            print(f"You've already guessed {guess}")
        else:
            print("Invalid input. Please enter a single letter.")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

while True:
    hangman()
    if not play_again():
        print("Thanks for playing!")
        break
        