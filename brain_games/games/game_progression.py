import prompt
import random

from brain_games.functions.calculations import find_missing


def game_progression():
        start = random.randint(1, 99)
        step = random.randint(1, 10)
        missing = random.randint(0, 9)
        progression = []
        for i in range(10):
            progression.append(start + step * i)
        progression[missing] = '..'

        question = ' '.join(str(e) for e in progression)

        correct_answer = find_missing(progression, step)

        return (question, correct_answer)
