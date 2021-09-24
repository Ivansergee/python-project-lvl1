#!/usr/bin/env python

from brain_games.games.game_calc import game_calc
from brain_games.games.game import game


def main():
    title = 'What is the result of the expression?'
    game(title, game_calc)


if __name__ == '__main__':
    main()
