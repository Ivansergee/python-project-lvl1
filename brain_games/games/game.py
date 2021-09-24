import prompt

from brain_games.functions.welcome import welcome_user


def game(title, question_generator):
    name = welcome_user()
    print(title)
    correct_count = 0
    while correct_count < 3:
        question, correct_answer = question_generator()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            correct_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa
            print(f"Let's try again {name}")
            break
    else:
        print(f'Congratulations, {name}!')
