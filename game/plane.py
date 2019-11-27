"""
                                     The base class of aircraft
Our aircraft hostile     small aircraft hostile     medium aircraft hostile     large aircraft
"""
import random

import pygame

import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """"
    The class of plane
    """
    # images of plane
    plane_images = []
    # images of plane exploding
    destroy_images = []
    # address of plane exploding music
    down_sound_src = None
    # situation of plane: True，alive，False, exploded
    active = True
    # plane fires the bullet sprite group
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        # load static resources
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()

        # speed
        self.speed = speed or 1
        # position
        self.rect = self.img_list[0].get_rect()

        # hight and weight of plane
        self.plane_w, self.plane_h = self.img_list[0].get_size()

        # hight and weight of game screen
        self.width, self.height = self.screen.get_size()

        # change the initial position of the aircraft to the bottom of the screen
        self.rect.left = int((self.width - self.plane_w) / 2)
        self.rect.top = int(self.height / 2)

    def load_src(self):
        """ load static resources """
        # images of plane
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))
        # images of plane exploding
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))
        # music of plane exploding
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """ plane moves upwards """
        self.rect.top -= self.speed

    def move_down(self):
        """ plane moves downwards """
        self.rect.top += self.speed

    def move_left(self):
        """ plane moves leftwards """
        self.rect.left -= self.speed

    def move_right(self):
        """ plane moves rightwards """
        self.rect.left += self.speed

    def broken_down(self):
        """ music of plane exploding """
        # 1. play music
        if self.down_sound:
            self.down_sound.play()
        # 2. play images
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        # 3. after exploding
        self.active = False

    def shoot(self):
        """ shoot bullet """
        bullet = Bullet(self.screen, self, 40)
        self.bullets.add(bullet)


class OurPlane(Plane):
    """ ourplane """
    # images of plane
    plane_images = constants.OUR_PLANE_IMG_LIST
    # images of plane exploding
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    # address of plane exploding music
    down_sound_src = None

    def update(self, war):
        """ update aircraft animation """
        self.move(war.key_down)
        # 1. toggle aircraft animation, jet effects
        if war.frame % 2:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)
        # aircraft impact detection
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        if rest:
            # 1. game end
            war.status = war.OVER
            # 2. enemy aircraft clearance
            war.enemies.empty()
            war.small_enemies.empty()
            # 3. our aircraft crash effect
            self.broken_down()
            # 4. record score

    def move(self, key):
        """ automatic aircraft movement control """
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        """ move up, out of range, adjust """
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        super().move_down()
        if self.rect.top >= self.height - self.plane_h:
            self.rect.top = self.height - self.plane_h

    def move_left(self):
        super().move_left()
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left >= self.width - self.plane_w:
            self.rect.left = self.width - self.plane_w


class SmallEnemyPlane(Plane):
    """ small enemy plane """
    plane_images = constants.SMALL_ENEMY_PLANE_IMG_LIST
    destroy_images = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    down_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND

    def __init__(self, screen, speed):
        super().__init__(screen, speed)
        # Each time you generate a new small plane, a random location appears on the screen
        # Change the random position of the plane
        self.init_pos()

    def init_pos(self):
        """ change the random position of the plane """
        self.rect.left = random.randint(0, self.width - self.plane_w)
        self.rect.top = random.randint(-2 * self.plane_h, -self.plane_h)

    def update(self, *args):
        """ update aircraft movement """
        super().move_down()

        self.blit_me()

        # beyond the scope
        if self.rect.top >= self.height:
            self.active = False
            # self.kill()
            self.reset()
        # todo 2. 多线程、多进程

    def reset(self):
        """ reset """
        self.active = True
        # change position
        self.init_pos()

    def broken_down(self):
        """ exploding """
        super().broken_down()
        self.reset()