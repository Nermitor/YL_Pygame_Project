import pygame as pg

from ui.button import OnlyImageButton
from ui.config import common_pause_menu_scale_factor, buttons_pause_menu_scale_factor
from ui.presets import game_play, game_home, game_reset
from ui.windows.game_menu import AbstractMenu
from userevents import GAME_EVENT_TYPE


class PauseMenu(AbstractMenu):
    def __init__(self, *args):
        self.text = "Игра остановлена"
        super().__init__(*args)

    def init_widgets(self):
        buttons_y = 350 * common_pause_menu_scale_factor
        self.resume_btn = game_play(self.image.get_width() // 2, buttons_y,
                                    init_scaling=buttons_pause_menu_scale_factor,
                                    addictions=(True, False))
        self.home_btn = game_home(self.image.get_width() // 2 + 100 * common_pause_menu_scale_factor, buttons_y,
                                  init_scaling=buttons_pause_menu_scale_factor,
                                  addictions=(True, False))
        self.reset_btn = game_reset(self.image.get_width() // 2 - 100 * common_pause_menu_scale_factor, buttons_y,
                                    init_scaling=buttons_pause_menu_scale_factor,
                                    addictions=(True, False))
        self.widgets = pg.sprite.Group(self.resume_btn, self.home_btn, self.reset_btn)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            for widget in self.widgets:
                if isinstance(widget, OnlyImageButton):
                    widget.handle_event(event)
        elif event.type == GAME_EVENT_TYPE:
            data = event.data
            if data['type'] == "button_click":
                if data['button'] == "game_play":
                    self.parent.frieze_scene(False)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.parent.frieze_scene(False)
