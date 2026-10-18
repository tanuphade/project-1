import random

# 5 predefined words
words = ["python", "computer", "program", "keyboard", "developer"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.\n")

# Main game loop
while wrong_guesses < max_wrong_guesses:
    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the player has guessed the entire word
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    # Add guess to the list
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

# If player reaches 6 incorrect guesses
if wrong_guesses == max_wrong_guesses:
    print("Game Over!")
    print("The word was:", word)
