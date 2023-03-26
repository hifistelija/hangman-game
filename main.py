import random
from hangman_words import word_list
import hangman_art

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
used_letters = set()

print(hangman_art.logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter")
    else:
        used_letters.add(guess)

    # Check guessed letter
    for index, letter in enumerate(chosen_word):
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[index] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} is not in the word. You have {lives} left.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])
