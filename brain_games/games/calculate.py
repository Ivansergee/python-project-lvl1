import prompt
import random


def summ(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def calculate():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    operators = ['*', '+', '-']
    correct_count = 0
    while correct_count < 3:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        operator = random.choice(operators)
        print(f'Question: {number1} {operator} {number2}')
        answer = prompt.integer('Your answer: ')

        if operator == '*':
            correct_answer = mult(number1, number2)
        elif operator == '+':
            correct_answer = summ(number1, number2)
        elif operator == '-':
            correct_answer = substract(number1, number2)

        if answer == correct_answer:
            correct_count += 1
            print('Correct!')
        else:
            correct_count = 0
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa
            print(f"Let's try again {name}")
    print(f'Congratulations, {name}!')
