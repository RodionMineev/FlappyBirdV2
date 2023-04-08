import pygame as pg
import os

setting = {
    'w': 800,
    # ширина
    'h': 800,
    # высота
    'title': 'Test',
    # название
    'fps': 60,
    # количество кадров в секунду
}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')

player_img = pg.image.load(os.path.join(media_folder, 'flappy.png'))
object_img = pg.image.load(os.path.join(media_folder, 'STOLB.png'))
FON_img = pg.image.load(os.path.join(media_folder, 'FON.jpg'))