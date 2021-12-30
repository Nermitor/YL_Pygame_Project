import pygame as pg


class AbstractButton(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, call_back_function: callable):
        super().__init__()
        self.call_back_function = call_back_function
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y

    def update(self, event: pg.event.Event):
        if self.rect.collidepoint(*event.pos):
            self.call_back_function()
