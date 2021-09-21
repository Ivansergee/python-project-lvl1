import prompt
import random

from ..functions.welcome import welcome_user
from ..functions.calculations import calculate
from ..functions.check_answer import check_answer


def game_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    operators = ['*', '+', '-']
    correct_count = 0
    while correct_count < 3:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        operator = random.choice(operators)
        print(f'Question: {number1} {operator} {number2}')
        answer = prompt.integer('Your answer: ')

        correct_answer = calculate(number1, number2, operator)

        if check_answer(answer, correct_answer):
            correct_count += 1
        else:
            correct_count = 0
            print(f"Let's try again {name}")

    print(f'Congratulations, {name}!')
