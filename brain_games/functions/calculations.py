import math


def find_gcd(number1, number2):
    number1, number2 = max(number1, number2), min(number1, number2)
    while number1 % number2 != 0:
        number1, number2 = (number2, number1 % number2)
    return number2


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2


def find_missing(progression, step):
    missing_i = progression.index('..')
    if missing_i > 0:
        return progression[missing_i - 1] + step
    else:
        return progression[missing_i + 1] - step


def is_prime(number):
    n = math.floor(math.sqrt(number))
    for i in range(2, n+1):
        if number % i == 0:
            return 'no'
    return 'yes'
