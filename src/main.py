
import pygame
from settings import *
from player import Player
from levelManager import LevelManager
from gameUI import GameUI
from gameManager import GameManager


if __name__ == "__main__":
    game = GameManager()
    game.run()
