from entities.camera.camera import Camera
from scenes.metascene import MetaScene
from ui.game_interface import UITimer
from ui.presets import *
from config.config_file import common_config
from utils.maploader import Map


class GameScene(MetaScene):
    def __init__(self, map_name: str):
        self.game_map = Map(map_name)

        self.platforms_group = self.game_map.sprites['platforms']
        self.player_group = pg.sprite.Group(self.game_map.get_player())
        self.ui_group = pg.sprite.Group()
        self.check_points = self.game_map.sprites['check_points_group']

        self.player = self.player_group.sprites()[0]
        self.bg = self.game_map.get_bg()
        self.timer = UITimer(common_config['common']['screen_size'][0])
        self.pause_button = game_pause(50, 30)

        self.ui_group.add(self.timer, self.pause_button)
        self.camera = Camera(*common_config['common']['screen_size'])

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

    def set(self):
        self.timer.start()

    def unset(self):
        self.timer.stop()
        self.timer.reset()

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        for group in self.all_groups:
            group.draw(screen)

    def update(self, *args, **kwargs):
        if not self.friezed:
            for group in self.all_groups:
                group.update(platforms=self.platforms_group, check_points=self.check_points)

        self.camera.update(self.player)
        for group in self.no_static_groups:
            for sprite in group:
                self.camera.apply(sprite)

    def handle_event(self, event):
        if event.type == GAME_EVENT_TYPE:
            data = event.data
            if data['type'] == "get_finish":
                generate_event(SCENE_AGGREGATOR_EVENT_TYPE, data={
                    "type": "switch_scene",
                    "scene": "menu"
                })
            elif data['type'] == "button_click":
                if data['button'] == 'game_pause':
                    self.friezed ^= 1
        elif event.type == pg.MOUSEBUTTONDOWN:
            for widget in self.ui_group:
                widget.handle_event(event)
