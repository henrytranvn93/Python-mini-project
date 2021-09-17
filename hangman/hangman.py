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

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        

user_input = input('Type something: ')
print