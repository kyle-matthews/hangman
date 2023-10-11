import random
word_list = ["melon", "grape", "banana", "apple", "pineapple"]
print(word_list)

def random_choice(list):
    word = random.choice(word_list) 
    print("word")

word = random_choice(word_list)

letter_guess = input("Enter a single letter...")

if (len(letter_guess) == 1) and (letter_guess.isalpha() == True):
    print("Good guess!")
else:
    print("Oops! That is not a valid input!")

while True:
    guess = input("Guess a letter.")

    if guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please enter a single alphabetical character.")


if guess in word:
        print(f"Good guess! {guess} is in the word")
    
else:
    print(f"Sorry, {guess} is not in the word. Try again.")