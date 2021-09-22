import prompt
import random

from brain_games.functions.calculations import is_even
from brain_games.functions.welcome import welcome_user
from brain_games.functions.check_answer import check_answer


def guess_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    while correct_count < 3:
        number = random.randint(1, 99)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        correct_answer = is_even(number)

        if check_answer(answer, correct_answer):
            correct_count += 1
        else:
            correct_count = 0
            print(f"Let's try again {name}")
    print(f'Congratulations, {name}!')
