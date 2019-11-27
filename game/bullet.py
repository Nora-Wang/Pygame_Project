import pygame
import constants


class Bullet(pygame.sprite.Sprite):

    # situation of bullet，True: alive
    active = True

    def __init__(self, screen, plane, speed=None):
        super().__init__()
        self.screen = screen
        # speed
        self.speed = speed or 4
        self.plane = plane

        # load the pict of bullet
        self.image = pygame.image.load(constants.BULLET_IMG)

        # change the position of bullet
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        # music for shooting
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, war):
        """ update the position of bullet """
        self.rect.top -= self.speed
        # out of screen range
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
            print(self.plane.bullets)
        # describe the bullet
        self.screen.blit(self.image, self.rect)
        # collision detection to see if the bullet has hit the enemy aircraft
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        for r in rest:
            # 1. bullet disappear
            self.kill()
            # 2. broken
            r.broken_down()
            # 3. count game scores
            war.rest.score += constants.SCORE_SHOOT_SMALL
            # save the score
            war.rest.set_history()


