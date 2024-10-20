from words import words
import random
import string

def get_word(words):
    word = random.choice(words)
    return (word.upper())


def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet  = set(string.ascii_uppercase)
    used_letter = set()

    

get_word(words)