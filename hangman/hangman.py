import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print(f'You have {lives} lives left')

        print('You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else: 
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You already guessed that character')
        
        else:
            print('Invalid character')
    if lives == 0: 
        print(f'You died!!! The word was {word}')
    else:
        print(f'You guessed the word {word}!!! Congrats!!!')
        

hangman()