import pygame
import sys

import constants
from game.plane import OurPlane, SmallEnemyPlane
from store.result import PlayRest


class PlaneWar(object):
    """ Aircraft War Game """
    # situation of game
    READY = 0
    PLAYING = 1
    OVER = 2
    status = READY

    our_plane = None

    frame = 0

    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # result of the game
    rest = PlayRest()

    def __init__(self):
        pygame.init()
        self.width, self.height = 480, 852
        self.screen = pygame.display.set_mode((self.width, self.height))
        #name of window
        pygame.display.set_caption('Aircraft Game')

        # load background images
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)
        # title
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()

        # start button
        self.btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
        self.btn_start_rect = self.btn_start.get_rect()
        btn_width, btn_height = self.btn_start.get_size()
        self.btn_start_rect.topleft = (int((self.width - btn_width) / 2),
                                  int(self.height / 2 + btn_height))

        # font
        self.score_font = pygame.font.SysFont('test_sans', 32)

        # load music
        pygame.mixer.music.load(constants.BG_MUSIC)
        pygame.mixer.music.play(-1)         # infinite loop for playing music
        pygame.mixer.music.set_volume(0.2)  # set the volume

        # our plane
        self.our_plane = OurPlane(self.screen, speed = 40)

        self.clock = pygame.time.Clock()

        # use keyboard to control aircraft
        self.key_down = None

    def bind_event(self):
        # 1. listening event
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # click the mouse to get in the game
                if self.status == self.READY:
                    self.status = self.PLAYING
                    self.rest.score = 0
                elif self.status == self.PLAYING:
                    # click the mouse to fire the bullet
                    self.our_plane.shoot()
                elif self.status == self.OVER:
                    self.status = self.READY
                    self.add_small_enemies(20)
            elif event.type == pygame.KEYDOWN:
                # keyborad
                self.key_down = event.key
                # only in the game, need to control the keyboard ASWD
                if self.status == self.PLAYING:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        # shoot
                        self.our_plane.shoot()

    def add_small_enemies(self, num):
        """
        add small enemy aircraft at random
        :param num: number of aircraft produced
        :return:
        """
        # add 6 small enemy aircraft at random
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 10)
            plane.add(self.small_enemies, self.enemies)

    def run_game(self):
        """ main part of game """
        while True:
            # 1. set the frame rate
            self.clock.tick(10)
            self.frame += 1
            if self.frame >= 10:
                self.frame = 0
            # 2. bind event
            self.bind_event()

            # 3.update the situation of game
            if self.status == self.READY:
                # get ready
                # setting background
                self.screen.blit(self.bg, self.bg.get_rect())
                # title
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                # start button
                self.screen.blit(self.btn_start, self.btn_start_rect)
                self.key_down = None
            elif self.status == self.PLAYING:
                # playing
                # background
                self.screen.blit(self.bg, self.bg.get_rect())
                # plane
                self.our_plane.update(self)
                # bullet
                self.our_plane.bullets.update(self)
                # enemy plane
                self.small_enemies.update()
                # score
                score_text = self.score_font.render(
                    'Score: {0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SOCRE_COLOR
                )
                self.screen.blit(score_text, score_text.get_rect())

            elif self.status == self.OVER:
                # end game
                # background
                self.screen.blit(self.bg_over, self.bg_over.get_rect())
                # account score
                # 1. total score
                score_text = self.score_font.render(
                    '{0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SOCRE_COLOR
                )
                self.screen.blit(score_text, (350,520))

                # 2. the highest score
                score_his = self.score_font.render(
                    '{0}'.format(self.rest.get_max_core()),
                    False,
                    constants.TEXT_SOCRE_COLOR
                )
                self.screen.blit(score_his, (350,300))

            pygame.display.flip()
