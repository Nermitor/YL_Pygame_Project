"""Меню окончания уровня"""

import pygame as pg

from ui.button import OnlyImageButton
from ui.config import common_pause_menu_scale_factor, buttons_pause_menu_scale_factor
from ui.presets import game_home, game_reset, game_next_level
from ui.windows.game_menu import AbstractMenu


class FinishMenu(AbstractMenu):
    def __init__(self, *args):
        self.text = "Уровень пройден"
        super().__init__(*args)

    def init_widgets(self):
        buttons_y = 350 * common_pause_menu_scale_factor

        self.home_btn = game_home(self.image.get_width() // 2 + 100 * common_pause_menu_scale_factor, buttons_y,
                                  init_scaling=buttons_pause_menu_scale_factor,
                                  addictions=(True, False))
        self.reset_btn = game_reset(self.image.get_width() // 2 - 100 * common_pause_menu_scale_factor, buttons_y,
                                    init_scaling=buttons_pause_menu_scale_factor,
                                    addictions=(True, False))
        self.widgets = pg.sprite.Group(self.home_btn, self.reset_btn)

        if self.parent.map_num < self.parent.levels_data['max_level']:
            self.next_level_btn = game_next_level(self.image.get_width() // 2, buttons_y,
                                                  init_scaling=buttons_pause_menu_scale_factor,
                                                  addictions=(True, False))
            self.widgets.add(self.next_level_btn)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            for widget in self.widgets:
                if isinstance(widget, OnlyImageButton):
                    widget.handle_event(event)
