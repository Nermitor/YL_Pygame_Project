import pygame as pg


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((100, 20))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
