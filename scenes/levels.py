"""Сцена с выбором уровней"""

import pygame as pg

from config.config import config
from scenes.metascene import MetaScene
from ui.presets import menu_back, empty_button
from userevents import generate_event_function, SCENE_AGGREGATOR_EVENT_TYPE
from utils.jsonio import JsonIO
from utils.levels import get_levels

font = pg.font.Font("ui/resources/fonts/standard.ttf", 80)


class Levels(MetaScene):
    """Окно с выбором уровней"""
    def __init__(self):
        self.bg = pg.image.load("scenes/resources/menu_bg.jpg").convert()
        self.back_btn = menu_back(120, 900)
        self.all_widgets = pg.sprite.Group(
            self.back_btn
        )

    def draw(self, screen):
        """Отрисовка сцены"""
        screen.blit(self.bg, (0, 0))
        self.all_widgets.draw(screen)

    def set(self):
        self.generate_levels_buttons()

    def handle_event(self, event):
        """Обработка событий"""
        for widget in self.all_widgets.sprites():
            widget.handle_event(event)

    def generate_levels_buttons(self):
        """Инициализация кнопок"""
        data = JsonIO("config/temp.json")
        passed_levels = data['unlocked_levels']
        scale_factor = config['common']['scale_factor']
        start_x, start_y = 20 * scale_factor, 30 * scale_factor
        step_x, step_y = 20 * scale_factor, 20 * scale_factor
        spacing_x = 100

        cur_x, cur_y = start_x, start_y

        for level in get_levels():
            # color = pg.Color("white" if level in unlocked_levels else "gray")
            # text_surface = font.render(str(level), False, color)
            if level in passed_levels:
                color = pg.Color("white")
                func = generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                    'type': "game_scene_from_num",
                    "level_num": level
                })
            else:
                color = pg.Color("gray")
                func = lambda *args, **kwargs: 0

            text_surface = font.render(str(level), False, color)
            button = empty_button(cur_x, cur_y, func)
            button.image.blit(text_surface, (40, 5))
            self.all_widgets.add(button)
            cur_x += step_x + spacing_x

