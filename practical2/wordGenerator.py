import random

def errorCheck():
    for letter in word_format:
        if letter == 'c' or letter == 'v':
            return True
        else:
            return False

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = str(input("Please enter c for consonants or v or vowels.").lower())

while not errorCheck():
    print("Error!")
    word_format = str(input("Please enter c for consonants or v or vowels.").lower())

word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == 'v':
        word += random.choice(VOWELS)
    else:
        print("error")

print(word)
