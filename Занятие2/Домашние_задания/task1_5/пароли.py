from string import ascii_lowercase, ascii_uppercase, digits
import random
while True:
    length = 8
    pas = ''
    for x in range(length):
        pas = pas + random.choice(ascii_lowercase)
        pas += random.choice(ascii_uppercase)
        pas += random.choice(digits)
    if length <
