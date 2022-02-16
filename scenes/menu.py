import pygame as pg

from config.config_file import common_config
from scenes.metascene import MetaScene
from ui.presets import menu_start, menu_exit, menu_music

screen_width, screen_height = common_config['common']['screen_size']


class MainMenu(MetaScene):
    def __init__(self):
        self.bg = pg.image.load("scenes/resources/menu_bg.jpg").convert()
        self.start_btn = menu_start(screen_width // 2, 300)
        self.ext_btn = menu_exit(screen_width // 2, 700)
        self.music_btn = menu_music(1800, 900)

        self.all_widgets = pg.sprite.Group(
            self.start_btn,
            self.ext_btn,
            self.music_btn
        )

    def unset(self):
        pass

    def set(self):
        pass

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        self.all_widgets.draw(screen)

    def update(self):
        pass

    def handle_event(self, event):
        for widget in self.all_widgets.sprites():
            widget.handle_event(event)
