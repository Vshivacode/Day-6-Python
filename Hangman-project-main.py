# Day-7: Hangman Project
from hangman_words_list import word_list
from hangman_images import logo, stages
import random

# Display Hangman game logo
print(logo)

# Choose a random word from the list
chosen_word = random.choice(word_list)

# Initialize the display with underscores
display = []
for char in chosen_word:
    display += "_"

# Set initial number of lives
lives = 6

# Main game loop
end_of_game = False
while not end_of_game:

    # Get user input for a guessed letter
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    # If the guessed letter is not in the chosen word, reduce lives
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You Lose. The chosen word is: {chosen_word}")

    # Display the current state of the word with underscores and guessed letters
    print(" ".join(display))

    # Check if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You Won")

    # Display the Hangman stage corresponding to the remaining lives
    print(stages[lives])
