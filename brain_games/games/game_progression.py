import prompt
import random

from ..functions.welcome import welcome_user
from ..functions.check_answer import check_answer
from ..functions.calculations import find_missing


def game_progression():
    name = welcome_user()
    print('What number is missing in the progression?')

    correct_count = 0
    while correct_count < 3:
        start = random.randint(1, 99)
        step = random.randint(1, 10)
        missing = random.randint(0, 9)
        progression = []
        for i in range(10):
            progression.append(start + step * i)
        progression[missing] = '..'
        print(f"Question: {' '.join(str(e) for e in progression)}")

        answer = prompt.integer('Your answer: ')

        correct_answer = find_missing(progression, step)

        if check_answer(answer, correct_answer):
            correct_count += 1
        else:
            correct_count = 0
            print(f"Let's try again {name}")

    print(f'Congratulations, {name}!')
