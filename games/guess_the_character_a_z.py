import os
from time import sleep
from random import choice
from string import ascii_lowercase

random_char = choice(ascii_lowercase)
tries = 0

command = 'cls' if os.name == 'nt' else 'clear'

def clear_screen():
    sleep(.3)
    os.system(command)

while True:
    guess = input('Guess the character (a-z): ')
    tries += 1
    
    clear_screen()
    
    if guess == random_char:
        break

print(f'Congrats, you have guessed the correct char \'{random_char}\' in {tries} tries.')
