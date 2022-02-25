import pygame as pg

from config.config import config
from utils.image import scalex

common = config['common']
check_points = config['environment']['platforms']

scale_factor = common['scale_factor'] * check_points['scale_factor']


class AbstractCheckPoint(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = scalex(image, scale_factor)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * scale_factor, (y + 5) * scale_factor

    @staticmethod
    def from_tile_cords(tile_cords, tile_size, image):
        tile_x, tile_y = tile_cords
        tile_width, tile_height = tile_size
        return __class__(tile_x * tile_width, tile_y * tile_height, image)
