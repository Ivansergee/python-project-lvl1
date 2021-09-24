import prompt
import random


def game_even():
    number = random.randint(1, 99)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)