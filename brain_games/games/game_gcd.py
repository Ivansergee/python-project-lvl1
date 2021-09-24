import prompt
import random

from brain_games.functions.calculations import find_gcd


def game_gcd():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    
    question = f'Question: {number1} {number2}'
    correct_answer = find_gcd(number1, number2)
    
    return (question, correct_answer)
