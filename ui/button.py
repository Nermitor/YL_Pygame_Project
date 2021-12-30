import pygame as pg

from .metaclases.abstarct_button import AbstractButton


class TextButton(AbstractButton):
    def __init__(self, x: int, y: int, text: str,
                 font: pg.font.Font, color: pg.Color, call_back_function: callable):
        self.image = font.render(text, False, color)
        self.rect = self.image.get_rect()
        self.color = color
        super().__init__(x, y, call_back_function)


class ImageButton(AbstractButton):
    def __init__(self, x: int, y: int, image: pg.Surface, call_back_function: callable):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y
        super().__init__(x, y, call_back_function)
