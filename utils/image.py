"""Содержит функцию масштабирования интерфейса"""

import pygame as pg


def scalex(image: pg.Surface, scale_factor: int):
    return pg.transform.scale(image, (image.get_width() * scale_factor, image.get_height() * scale_factor))
