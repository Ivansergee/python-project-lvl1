#!/usr/bin/env python

from brain_games.games.game_progression import game_progression
from brain_games.games.game import game


def main():
    title = 'What number is missing in the progression?'
    game(title, game_progression)


if __name__ == '__main__':
    main()
