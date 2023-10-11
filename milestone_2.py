import random
word_list = ["melon", "grape", "banana", "apple", "pineapple"]
print(word_list)

def random_choice(choice):
    word = random.choice(word_list)
    print(word)

random_choice(word_list)

letter_guess = input("Enter a single letter...")

if (len(letter_guess) == 1) and (letter_guess.isalpha() == True):
    print("Good guess!")
else:
    print("Oops! That is not a valid input!")