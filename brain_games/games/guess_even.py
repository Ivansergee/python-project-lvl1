import prompt
import random

from .welcome import welcome_user
from .check_answer import check_answer


def guess_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    while correct_count < 3:
        number = random.randint(1, 99)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if check_answer(answer, correct_answer):
            correct_count += 1
        else:
            correct_count = 0
            print(f"Let's try again {name}")
    print(f'Congratulations, {name}!')
