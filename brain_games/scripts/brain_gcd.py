#!/usr/bin/env python

from brain_games.games.game_gcd import game_gcd
from brain_games.games.game import game


def main():
    title = 'Find the greatest common divisor of given numbers.'
    game(title, game_gcd)


if __name__ == '__main__':
    main()
