import random


# Gut user's name
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the guessing game.")

# List of words
words = ["python", "programming", "computer", "algorithm", "function", "variable", "loop", "condition"]


# Select a random word from the list
word = random.choice(words)

print("\nGuess the charaters")

# Store guessed characters
guesses = ''

# Number of attempts
turns = 12

# Main game loop
while turns > 0:

    # Flag to check if the word is guessed
    failed = 0

    # Display guessed characters and hidden letters
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed +=1
    print()

    # Check if the word has been guessed
    if failed == 0:
        print("You Win")
        print("The word is:", word)
        break

    # Get user input
    guess = input("Guess a character: ").lower()

    # Validation input length
    if len(guess) != 1:
        print("Please enter a sigle character.")
        continue
    # Check for duplicate guesses
    if guess in guesses:
        print("You already guessed that charcter.")
        continue

    # Store the guess
    guesses += guess

    # Handle incorrect guesses
    if guess not in word:
        turns -= 1
        print("Worng")
        print("You have", turns, "more guesses")

        if turns == 0:
            print("You Lose")
            print("The word was:", word)     





