import pygame as pg

from entities.player.animations.animation import anims, new_size
from utils.jsonreader import JsonReader

individual = JsonReader("entities/player/config.json")["physics"]
common = JsonReader("entities/config.json")['physics']

DEFAULT_DIR = individual['default_dir']
MOVE_SPEED = individual["move_speed"]
JUMP_POWER = individual["jump_power"]
GRAVITY = common["gravity"]


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface(new_size)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.dir = DEFAULT_DIR
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.isFly = False

        self.anim = anims[self.dir]['idle']

    # update()

    def update(self, platforms):
        keys = pg.key.get_pressed()
        left = keys[pg.K_a]
        right = keys[pg.K_d]
        up = keys[pg.K_SPACE]

        self.xvel = 0

        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER

        if left:
            self.xvel = -MOVE_SPEED
            self.dir = -1

        if right:
            self.xvel = MOVE_SPEED
            self.dir = 1

        if self.isFly:
            if self.yvel > 0:
                self.anim = anims[self.dir]['fall']
            else:
                self.anim = anims[self.dir]['jump']
        else:
            self.anim = anims[self.dir]['run']

        if not (left or right) and not self.isFly:
            self.xvel = 0
            self.anim = anims[self.dir]['idle']

        if not self.onGround:
            self.yvel += GRAVITY

        if abs(round(self.yvel)) > 2:
            # print("В воздухе")
            self.isFly = True

        elif self.onGround:
            # print "Стоит"
            self.isFly = False

        self.image.fill("black")
        self.anim.play()
        self.anim.blit(self.image, (0, 0))
        self.image.set_colorkey("black")

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pg.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.xvel = 0

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.xvel = 0

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
