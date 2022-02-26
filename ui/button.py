"""Класс кнопки с изображением"""

from utils.image import scalex
from .metaclases.abstract_button import AbstractButton


class OnlyImageButton(AbstractButton):
    def __init__(self, x: int, y: int, image, call_back_function, scaling, **kwargs):
        self.image = scalex(image, scaling)
        if (addictions := kwargs.get("addictions")) is not None:
            x_addiction, y_addiction = addictions
            if not x_addiction:
                x *= scaling
            if not y_addiction:
                y *= scaling
        super().__init__(x, y, call_back_function)
