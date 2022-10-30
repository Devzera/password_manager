from random import choice
from string import ascii_letters, digits, punctuation


def generate_password(length, numbers, special):
    characters = ascii_letters
    if numbers:
        characters += digits
    if special:
        characters += punctuation
    password = ''
    for i in range(length):
        password += choice(characters)

    return password
