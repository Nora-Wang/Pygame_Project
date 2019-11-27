import pygame
import sys

import constants
from game.plane import OurPlane, SmallEnemyPlane
from game.war import PlaneWar


def main():
    """ begain game，main """
    war = PlaneWar()
    # add small Enemy aircraft
    war.add_small_enemies(15)
    war.run_game()


if __name__ == '__main__':
    main()
