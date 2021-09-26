import random

from brain_games.functions.calculations import is_prime


def game_prime():
    number = random.randint(1, 99)
    correct_answer = is_prime(number)

    return (number, correct_answer)
