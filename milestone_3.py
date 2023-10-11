import random
word_list = ["melon", "grape", "banana", "apple", "pineapple"]
print(word_list)

def random_choice(list):
    word = random.choice(word_list) 
    return word

word = random_choice(word_list)

while True:
    guess = input("Guess a letter.")

    if (len(guess) == 1) and (guess.isalpha() == True):
        if guess in word:
            print(f"Good guess! {guess} is in the word")
    
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
        
    else:
        print("Invalid letter. Please enter a single alphabetical character.")

