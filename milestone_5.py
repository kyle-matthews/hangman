import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for character in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives

        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")
            for character in guess:
                if character == guess:
                    for i in range(len(self.word)):
                        if self.word[i] == guess:
                            self.word_guessed[i] = guess    
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter...")
            if guess.isalpha() != True or len(guess) > 1:
                print("Invalid input. Please, enter a single alphabetical character.")
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while game.num_lives >= 0:    
        if game.num_lives == 0:
            print("You lost!")
            break

        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_letters == 0:
            print("Congratulations! You won the game!")
            break
        
    
        

word_list = ["melon", "banana", "apple", "lime", "kiwi", "dragonfruit", "pineapple"]
play_game(word_list)