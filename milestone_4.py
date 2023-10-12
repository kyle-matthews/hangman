import random

def ask_for_input():
    while True:
        guess = input("Guess a letter.").lower()
        
        if (len(guess) == 1) and (guess.isalpha() == True):
            if guess in word:
                check_guess(guess)
            else:
                print("Invalid letter. Please enter a single alphabetical character.")



ask_for_input()

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
    
    def ask_for_input():
        while True:
            guess = input("Guess a letter...")
            if guess.isalpha() != True:
                print("Invalid letter. Please, enter a single aplphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
