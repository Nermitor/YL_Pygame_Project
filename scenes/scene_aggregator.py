"""Менеджер сцен"""

from scenes.game_scene import GameScene
from scenes.levels import Levels
from scenes.menu import MainMenu
from userevents import *
from utils.jsonio import JsonIO


class SceneAggregator:
    """Класс менеджера сцен"""
    def __init__(self):
        self.cur_game_level = 1
        self.game_scene = GameScene(self.cur_game_level)
        self.levels_scene = Levels()

        self.levels_data = JsonIO("config/temp.json")

        self.menu_scene = MainMenu()

        self.cur_scene = None

        self.scenes = {
            "menu": self.menu_scene,
            "game": self.game_scene,
            "levels": self.levels_scene
        }

        self.set("menu")

    def switch_to(self, scene_name):
        """Смена с текущей сцены на другую"""
        self.cur_scene.unset()
        self.set(scene_name)

    def set(self, scene_name):
        """Установка сцены"""
        self.cur_scene = self.scenes[scene_name]
        self.cur_scene.set()

    def draw_cur_scene(self, screen):
        """Отрисовка текущей сцены"""
        self.cur_scene.draw(screen)

    def update_cur_scene(self, *args, **kwargs):
        """Обновление текущей смены"""
        self.cur_scene.update(*args, **kwargs)

    def handle_event(self, event):
        """Обработка событий"""
        if event.type == SCENE_AGGREGATOR_EVENT_TYPE:
            # Обработка событий менеджера сцен
            data = event.data
            if data['type'] == "switch_scene":
                self.switch_to(data['scene'])
            elif data['type'] == 'next_game_level':
                self.cur_game_level += 1
                self.game_scene.__init__(self.cur_game_level)
                self.switch_to("game")
            elif data['type'] == "game_scene_from_num":
                self.game_scene.__init__(level := data['level_num'])
                self.cur_game_level = level
                self.switch_to("game")

        else:
            # Обработка событий сцены
            self.cur_scene.handle_event(event)
