import pygame as pg

from .metaclases.abstract_button import AbstractButton, AbstractTextWithImageButton


class OnlyImageButton(AbstractButton):
    def __init__(self, x: int, y: int, image: pg.Surface, call_back_function: callable):
        self.image = image
        super().__init__(x, y, call_back_function)


class OnlyTextButton(AbstractButton):
    def __init__(self, x: int, y: int, text: str, font: pg.font.Font, color: pg.Color, call_back_function: callable):
        self.image = font.render(text, False, color)
        super().__init__(x, y, call_back_function)


class TextButtonWithBGColor(AbstractTextWithImageButton):
    def __init__(self, x: int, y: int, width: int, height: int, text: str,
                 font: pg.font.Font, color: pg.Color, bg_color: pg.Color, call_back_function: callable):
        self.image = pg.Surface((width, height))
        self.image.fill(bg_color)
        super().__init__(x, y, text, font, color, call_back_function)


class TextButtonWithImage(AbstractTextWithImageButton):
    def __init__(self, x: int, y: int, text: str,
                 font: pg.font.Font, color: pg.Color, image: pg.Surface, call_back_function: callable):
        self.image = image
        super().__init__(x, y, text, font, color, call_back_function)
