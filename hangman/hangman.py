import random
from words import words
import string
from hangman_visual import lives_visual_dict
from hangman_visual import logo


print(logo)

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'Lives left: {lives}.  Letters guessed: ', ' '.join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        print("\n")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word. ")
        elif user_letter in used_letters:
            print("You have already guessed this letter. Please guess another letter")
        else:
            print("Invalid guess. Please type in an alphabetical character. ")
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"Sorry, you failed to guess the word {word} and fell to your demise. Better luck next time! ")
    else:
        print(f"Congratulations you guessed {word} correctly and still had {lives} lives left!!  ")
hangman()
