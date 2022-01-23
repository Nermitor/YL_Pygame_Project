import pygame as pg

from entities.player.animations.animation import anims, new_size
from entities.player.physics.physics import DEFAULT_DIR, JUMP_POWER, GRAVITY, MOVE_SPEED, total_scale_factor


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface(new_size)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * total_scale_factor, y * total_scale_factor

        self.dir = DEFAULT_DIR
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.isFly = False
        self.wall_check_point_large = 30

        self.default_jumps_count = 2
        self.jumps = self.default_jumps_count

        self.last_update_is_jump = False
        self.on_wall = False
        self.wall_slide_speed = 0.5

        self.timer = pg.time.Clock().tick

        self.anim = anims[self.dir]['idle']

    # update()

    def update(self, platforms):
        keys = pg.key.get_pressed()
        left = keys[pg.K_a]
        right = keys[pg.K_d]
        up = keys[pg.K_SPACE]

        self.xvel = 0

        if up:
            if self.on_wall and not self.last_update_is_jump:
                self.yvel = -JUMP_POWER
                self.last_update_is_jump = True
                self.on_wall = False
                self.jumps = self.default_jumps_count - 1
            else:
                if self.jumps and not self.last_update_is_jump:
                    self.yvel = -JUMP_POWER
                    self.jumps -= 1
                    self.last_update_is_jump = True

        self.last_update_is_jump = up

        if left:
            self.xvel = -MOVE_SPEED
            self.dir = -1

        if right:
            self.xvel = MOVE_SPEED
            self.dir = 1

        if left or right:
            self.on_wall = False

        if self.isFly:
            if self.on_wall:
                self.anim = anims[self.dir]['wall_slide']
            else:
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
            self.isFly = True

        elif self.onGround:
            self.isFly = False
            self.jumps = self.default_jumps_count
            self.on_wall = False

        self.image.fill("black")
        self.anim.play()
        self.anim.blit(self.image, (0, 0))
        self.image.set_colorkey("black")
        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        if self.xvel and self.yvel >= 0:
            self.on_wall = False

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

        self.wall_check(platforms)

        if self.on_wall:
            self.yvel = self.wall_slide_speed

    def collide(self, xvel, yvel, platforms: pg.sprite.Group):
        for p in platforms:
            self.factor = False
            if pg.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.xvel = 0
                    self.on_wall = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.xvel = 0
                    self.on_wall = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

    def wall_check(self, platforms: pg.sprite.Group):
        if self.on_wall:
            self.on_wall = False
            if self.dir == -1:
                cur_pos = self.rect.left - self.wall_check_point_large, self.rect.y + self.rect.height // 2
            else:
                cur_pos = self.rect.right + self.wall_check_point_large, self.rect.y + self.rect.height // 2
            for p in platforms:
                if p.rect.collidepoint(*cur_pos):
                    self.on_wall = True
                    return
