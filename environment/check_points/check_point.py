import pygame as pg

from config.config_file import common_config

common = common_config['common']
check_points = common_config['environment']['platforms']

scale_factor = common['scale_factor'] * check_points['scale_factor']


class AbstractCheckPoint(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pg.transform.scale(image, (image.get_width() * scale_factor, image.get_height() * scale_factor))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * scale_factor, y * scale_factor

    @staticmethod
    def from_tile_cords(tile_cords, tile_size, image):
        tile_x, tile_y = tile_cords
        tile_width, tile_height = tile_size
        return __class__(tile_x * tile_width, tile_y * tile_height, image)
