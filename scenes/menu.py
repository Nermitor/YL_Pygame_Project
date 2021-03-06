"""Сцена с главным меню"""

import pygame as pg

from config.config import config
from scenes.metascene import MetaScene
from ui.presets import menu_start, menu_exit, menu_music, menu_levels

screen_width, screen_height = config['common']['screen_size']


class MainMenu(MetaScene):
    """Главное меню игры"""
    def __init__(self):
        self.bg = pg.image.load("scenes/resources/menu_bg.jpg").convert()
        self.start_btn = menu_start(screen_width // 2, 300)
        self.ext_btn = menu_exit(screen_width // 2, 700)
        self.music_btn = menu_music(1800, 900)
        self.levels_btn = menu_levels(1800, 700)

        self.all_widgets = pg.sprite.Group(
            self.start_btn,
            self.ext_btn,
            self.music_btn,
            self.levels_btn
        )

    def draw(self, screen):
        """Отрисовка"""
        screen.blit(self.bg, (0, 0))
        self.all_widgets.draw(screen)

    def handle_event(self, event):
        """Обработка событий"""
        for widget in self.all_widgets.sprites():
            widget.handle_event(event)
