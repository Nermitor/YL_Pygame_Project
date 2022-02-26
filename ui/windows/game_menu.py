"""Класс абстрактного игрового меню"""

import pygame as pg

from scenes.metascene import MetaScene
from ui.config import common_pause_menu_scale_factor, pause_menu_font
from utils.image import scalex


class AbstractMenu(MetaScene):
    def __init__(self, x, y, parent):
        self.cords = [x, y]
        self.parent = parent
        self.image = scalex(pg.image.load("ui/resources/menu_sheet.png"), common_pause_menu_scale_factor).convert()
        self.image.set_colorkey(pg.Color("white"))
        self.cords[0] -= self.image.get_width() // 2
        self.init_widgets()
        self.set_text()
        self.sync_widgets_cords()

    def draw(self, screen):
        screen.blit(self.image, self.cords)
        self.widgets.draw(screen)

    def sync_widgets_cords(self):
        for widget in self.widgets:
            widget.rect.x += self.cords[0]
            widget.rect.y += self.cords[1]

    def set_text(self):
        self.text_surface = pg.sprite.Sprite(self.widgets)
        self.text_surface.image = scalex(pause_menu_font.render(self.text, False, pg.Color("white")),
                                         common_pause_menu_scale_factor)
        self.text_surface.rect = self.text_surface.image.get_rect()
        self.text_surface.rect.x, self.text_surface.rect.y = 50, 20

    def update(self, *args, **kwargs):
        ...

    def init_widgets(self):
        ...

    def handle_event(self, event):
        ...
