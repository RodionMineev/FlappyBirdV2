from  setting import *


class Objeckt(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.speedx = None
        self.image = object_img
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def update(self):

            self.speedx = 5
            if self.rect.x != 0:
                self.rect.x -= self.speedx
            else:
                self.kill()