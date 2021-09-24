#!/usr/bin/env python

from brain_games.games.game_even import game_even
from brain_games.games.game import game


def main():
    title = 'Answer "yes" if the number is even, otherwise answer "no".'
    game(title, game_even)


if __name__ == '__main__':
    main()
