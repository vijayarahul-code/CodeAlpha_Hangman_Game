import random

# Words for the game
word_list = ["apple", "python", "mobile", "laptop", "coding"]

# Choosing a random word
word = random.choice(word_list)

guessed = []
chances = 6

print("Welcome to Hangman Game")

while chances > 0:
    print("\nWord: ", end="")

    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    # Check if all letters are guessed
    completed = True

    for letter in word:
        if letter not in guessed:
            completed = False
            break

    if completed:
        print("You won the game!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already entered this letter.")
        continue

    if guess in word:
        guessed.append(guess)
        print("Correct guess!")
    else:
        chances = chances - 1
        print("Wrong guess!")
        print("Remaining chances:", chances)

if chances == 0:
    print("\nGame Over!")
    print("The correct word is:", word)