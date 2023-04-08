

from setting import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.speedx = None
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)
        self.radios = 10  

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        self.speedy = 0

        if keystate[pg.K_SPACE  ]:
            self.rect.y += -15

        if self.rect.x > setting["w"]-42:
            self.rect.x -= 10
        if self.rect.x < 0:
            self.rect.x += 10

        if self.rect.bottom < setting["h"]:
            self.rect.y += 5


        else:
            self.rect.bottom = setting["h"]

        if self.rect.top < 0:
            self.rect.top = 0

