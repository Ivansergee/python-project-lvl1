import prompt
import random

from brain_games.functions.welcome import welcome_user
from brain_games.functions.calculations import find_gcd
from brain_games.functions.check_answer import check_answer


def game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    correct_count = 0
    while correct_count < 3:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        print(f'Question: {number1} {number2}')
        answer = prompt.integer('Your answer: ')

        correct_answer = find_gcd(number1, number2)

        if check_answer(answer, correct_answer):
            correct_count += 1
        else:
            correct_count = 0
            print(f"Let's try again {name}")

    print(f'Congratulations, {name}!')
