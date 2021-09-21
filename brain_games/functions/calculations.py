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
