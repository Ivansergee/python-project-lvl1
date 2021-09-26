import random


def game_calc():
    operators = ['*', '+', '-']
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    operator = random.choice(operators)

    question = f'{number1} {operator} {number2}'

    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    elif operator == '*':
        correct_answer = number1 * number2

    return (question, correct_answer)
