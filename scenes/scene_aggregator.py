from scenes.game_scene import GameScene


class SceneAggregator:
    def __init__(self):
        self.game_scene = GameScene("maps/tiles/безымянный.tmx")

        self.scenes = {
            "game": self.game_scene
        }

        self.cur_scene = self.game_scene

    def switch_to(self, scene_name):
        self.cur_scene.unset()
        self.cur_scene = self.scenes[scene_name]
        self.cur_scene.set()

    def draw_cur_scene(self, screen):
        self.cur_scene.draw(screen)

    def update_cur_scene(self, *args, **kwargs):
        self.cur_scene.update(*args, **kwargs)

    def handle_event(self, event):
        self.cur_scene.handle_event(event)
