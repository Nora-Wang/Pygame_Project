import os
import pygame

# The root directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Static file directory
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# Background
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')
# Title
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
# Start button
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
# Music
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')
# Game score color
TEXT_SOCRE_COLOR = pygame.Color(20, 20, 20)
# Hit small aircraft adds 10 points
SCORE_SHOOT_SMALL = 10
# The location of the file where the game results are stored
PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, 'store/rest.txt')


# Static source of our aircraft
OUR_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero1.png'),
    os.path.join(ASSETS_DIR, 'images/hero2.png')
]
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png'),
]

# Pictures and sounds of bullets fired
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

# Enemy small aircraft pictures and sound effects
SMALL_ENEMY_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/enemy1.png')]
SMALL_ENEMY_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png'),
]
# Play music when a small plane crashes
SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(ASSETS_DIR, 'sounds/enemy1_down.wav')

