import pygame as pg
from config.config_file import common_config
from scenes.metascene import MetaScene
from ui.button import OnlyImageButton
from ui.presets import start, ext

screen_width, screen_height = common_config['common']['screen_size']

class MainMenu(MetaScene):
    def __init__(self):
        self.start_btn = start(screen_width // 2, 300)
        self.ext_btn = ext(screen_width // 2, 700)

        self.all_widgets = pg.sprite.Group(
            self.start_btn,
            self.ext_btn
        )

    def unset(self):
        pass

    def set(self):
        pass

    def draw(self, screen):
        self.all_widgets.draw(screen)

    def update(self):
        pass

    def handle_event(self, event):
        self.all_widgets.update(event)
