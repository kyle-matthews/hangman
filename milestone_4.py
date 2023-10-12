import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for character in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = ["melon", "grape", "banana", "apple", "pineapple"]
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter...")
            if guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in Hangman.list_of_guesses:
                print("You already tried that letter!")
            else:
                Hangman.check_guess(guess)
                Hangman.list_of_guesses.append(guess)

Hangman.ask_for_input()