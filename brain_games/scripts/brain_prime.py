#!/usr/bin/env python

from brain_games.games.game_prime import game_prime
from brain_games.games.game import game


def main():
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game(title, game_prime)


if __name__ == '__main__':
    main()
