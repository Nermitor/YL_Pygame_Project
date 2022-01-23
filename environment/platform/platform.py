import pygame as pg

from utils.jsonreader import JsonReader

common = JsonReader('common.json')
platform = JsonReader("environment/platform/config.json")

scale_factor = common['scale_factor'] * platform['scale_factor']


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, image: pg.Surface):
        super().__init__()
        self.image = pg.transform.scale(image, (image.get_width() * scale_factor, image.get_height() * scale_factor))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * scale_factor, y * scale_factor

    @staticmethod
    def from_tile_cords(tile_cords, tile_size, image):
        tile_x, tile_y = tile_cords
        tile_width, tile_height = tile_size
        return Platform(tile_x * tile_width, tile_y * tile_height, image)
