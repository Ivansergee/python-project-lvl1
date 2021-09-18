import prompt
import random


def guess_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
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

        if answer == correct_answer:
            correct_count += 1
            print('Correct!')
        else:
            correct_count = 0
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa
            print(f"Let's try again {name}")
    print(f'Congratulations, {name}!')
