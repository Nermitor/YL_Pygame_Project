"""Игровая сцена"""

import pygame as pg

from config.config import config
from entities.camera.camera import Camera
from scenes.metascene import MetaScene
from ui.config import timer_font
from ui.game_interface import UITimer
from ui.presets import game_pause
from ui.windows.finish_menu import FinishMenu
from ui.windows.pause_menu import PauseMenu
from userevents import GAME_EVENT_TYPE
from utils.jsonio import JsonIO
from utils.maploader import Map


class GameScene(MetaScene):
    def __init__(self, map_num):
        self.map_num = map_num

    def init(self):
        self.game_map = Map(f"maps/tiles/{self.map_num}.tmx")
        self.platforms_group = self.game_map.sprites['platforms']
        self.player_group = pg.sprite.Group(self.game_map.get_player())
        self.ui_group = pg.sprite.Group()
        self.check_points = self.game_map.sprites['check_points_group']

        self.player = self.player_group.sprites()[0]
        self.bg = self.game_map.get_bg()
        self.timer = UITimer(config['common']['screen_size'][0])
        self.timer.start()
        self.pause_button = game_pause(50, 30)

        self.ui_group.add(self.timer, self.pause_button)
        self.camera = Camera(*config['common']['screen_size'])
        self.pause_menu = PauseMenu(config['common']['screen_size'][0] // 2, 300, self)

        self.all_groups = [
            self.platforms_group,
            self.player_group,
            self.ui_group,
            self.check_points
        ]
        self.no_static_groups = [
            self.platforms_group,
            self.player_group,
            self.check_points
        ]
        self.static_groups = [
            self.ui_group
        ]
        self.friezed = False
        self.finished = False

        self.levels_data = JsonIO("config/temp.json")
        self.levels_data['last_level'] = self.map_num
        self.finish_menu = FinishMenu(config['common']['screen_size'][0] // 2, 300, self)

        self.cur_level_best_time = self.levels_data['best_time'].get(str(self.map_num))
        if self.cur_level_best_time is not None:
            ms_time = self.cur_level_best_time
            if ms_time >= 1000:
                text = f"Best time| {self.timer.get_time_s_text(ms_time)}"
            else:
                text = f"Best time| 0.{ms_time}s"
            self.cur_level_surface = timer_font.render(
                text, False, pg.Color("black"))

    def set(self):
        """Установка основных параметров для сцены"""
        self.init()

    def frieze_scene(self, value):
        """Заморозка сцены"""
        if value:
            self.timer.stop()
        else:
            self.timer.start()
        self.friezed = value

    def draw(self, screen):
        """Отрисовка сцены"""
        screen.blit(self.bg, (0, 0))
        for group in self.all_groups:
            group.draw(screen)
        if self.friezed:
            self.pause_menu.draw(screen)
        elif self.finished:
            self.finish_menu.draw(screen)

        if self.cur_level_best_time is not None:
            screen.blit(self.cur_level_surface, (1350, 900))

    def update(self, *args, **kwargs):
        """Обновление сцены"""
        if not self.friezed and not self.finished:
            for group in self.all_groups:
                group.update(platforms=self.platforms_group, check_points=self.check_points)

            self.camera.update(self.player)
            for group in self.no_static_groups:
                for sprite in group:
                    self.camera.apply(sprite)

    def handle_event(self, event):
        """Обработка ивента"""
        if self.friezed:
            self.pause_menu.handle_event(event)
        elif self.finished:
            self.finish_menu.handle_event(event)
        else:
            if event.type == GAME_EVENT_TYPE:
                data = event.data
                if data['type'] == "get_finish":
                    self.finished = True
                    self.levels_data["unlocked_levels"] = list({*self.levels_data['unlocked_levels'], self.map_num + 1})
                    d = self.levels_data.data
                    cur_level_time = self.levels_data['best_time'].get(str(self.map_num))
                    if cur_level_time is None:
                        d['best_time'][str(self.map_num)] = self.timer.get_time()
                    else:
                        d['best_time'][str(self.map_num)] = min(self.timer.get_time(), cur_level_time)

                    self.levels_data.save(d)

                elif data['type'] == "button_click":
                    if data['button'] == 'game_pause':
                        self.frieze_scene(self.friezed ^ 1)

            elif event.type == pg.MOUSEBUTTONDOWN:
                for widget in self.ui_group:
                    widget.handle_event(event)

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.frieze_scene(True)
