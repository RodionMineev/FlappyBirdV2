import random
from Player import Player
from setting import *
from Objeckt import Objeckt

pg.init()

screen = pg.display.set_mode((setting["w"], setting["h"]))
pg.display.set_caption(setting["title"])
clock = pg.time.Clock()

clock = pg.time.Clock()

object_group = pg.sprite.Group()
all_sprite = pg.sprite.Group()

player = Player()
all_sprite.add(player)

font = pg.font.SysFont('Arial', 90)
score_surface = font.render('0', True, (255, 255, 255))


def new_mobs():
    object_botom = Objeckt(setting['w'], random.randint(500, 900))
    object_top = Objeckt(setting['w'], random.randint(-100, 100))
    object_group.add(object_top, object_botom)
    all_sprite.add(object_group)



SPAWN_SPRITE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_SPRITE, 1500)

pg.time.set_timer(pg.USEREVENT, 50)

run = True
score = 0
while run:
    clock.tick(setting['fps'])
    pg.display.flip()
    screen.blit(FON_img ,(0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN_SPRITE:
            new_mobs()
            score = score + 1
        if event.type == pg.USEREVENT:
            score_surface = font.render(f"{score}", True, 'white')

        if pg.sprite.spritecollide(player, object_group, False, pg.sprite.collide_circle):
            run = False

    all_sprite.update()

    all_sprite.draw(screen)
    screen.blit(score_surface, (270, 20))
    pg.display.flip()

pg.quit()