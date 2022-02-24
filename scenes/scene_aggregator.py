from scenes.game_scene import GameScene
from scenes.menu import MainMenu
from userevents import *


class SceneAggregator:
    def __init__(self):
        self.cur_game_level = 1
        self.game_scene = GameScene(self.cur_game_level)

        self.menu_scene = MainMenu()

        self.cur_scene = None

        self.scenes = {
            "menu": self.menu_scene,
            "game": self.game_scene
        }

        self.set("menu")

    def switch_to(self, scene_name):
        self.cur_scene.unset()
        self.set(scene_name)

    def set(self, scene_name):
        self.cur_scene = self.scenes[scene_name]
        self.cur_scene.set()

    def draw_cur_scene(self, screen):
        self.cur_scene.draw(screen)

    def update_cur_scene(self, *args, **kwargs):
        self.cur_scene.update(*args, **kwargs)

    def handle_event(self, event):
        if event.type == SCENE_AGGREGATOR_EVENT_TYPE:
            data = event.data
            if data['type'] == "button_click":
                if data['button'] == "menu_start":
                    self.switch_to("game")
                elif data['button'] == 'menu_exit':
                    generate_event(pg.QUIT)
            elif data['type'] == "switch_scene":
                self.switch_to(data['scene'])
            elif data['type'] == 'next_game_level':
                try:
                    self.game_scene.__init__(self.cur_game_level + 1)
                    self.game_scene.init()
                except FileNotFoundError:
                    pass
                else:
                    self.cur_game_level += 1

        else:
            self.cur_scene.handle_event(event)
