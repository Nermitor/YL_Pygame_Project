from .player_animation import *

physics = JsonReader("entities/player/config.json")["physics"]
common = JsonReader("config.json")

DEFAULT_DIR = physics['default_dir']
MOVE_SPEED = physics["move_speed"]
JUMP_POWER = -physics["jump_power"]
GRAVITY = -physics["gravity"]
SCREEN_HEIGHT = common["screen_size"][1]


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface(new_size)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.anim = player_idle_anim_right
        self.anim.play()

        self.dir = DEFAULT_DIR
        self.xvel = 0
        self.yvel = 0
        self.on_ground = False

    # update()
