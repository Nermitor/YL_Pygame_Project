import pygame as pg

from entities.player.animations.animation import anims, new_size
from entities.player.physics.physics import DEFAULT_DIR, JUMP_POWER, GRAVITY, MOVE_SPEED, \
    FAST_RUN_SPEED, totalize
from userevents import GAME_EVENT_TYPE


class Player(pg.sprite.Sprite):
    """Класс спрайта игрока"""
    def __init__(self, x, y):
        """Инициализация спрайта"""
        super().__init__()
        self.image = pg.Surface(new_size)
        self.image.convert_alpha()
        self.rect = pg.Surface(new_size).get_rect()
        self.rect.x, self.rect.y = totalize(x), totalize(y)
        self.hit_box = self.rect.inflate((totalize(-15)), totalize(-10))
        self.hit_box_distance = totalize(4)

        self.dir = DEFAULT_DIR
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.isFly = False

        self.default_jumps_count = 2
        self.jumps = self.default_jumps_count
        self.last_update_is_jump = False

        self.wall_check_point_large_x = totalize(6)
        self.wall_check_point_large_y = totalize(6)
        self.on_wall = False
        self.wall_slide_speed = 0.5

        self.ground_check_point_large_x = totalize(6)
        self.ground_check_point_large_y = totalize(2)

        self.fast_run_speed = FAST_RUN_SPEED

        self.timer = pg.time.Clock().tick

        self.anim = anims[self.dir]['idle']

    # update()

    def update(self, *args, **kwargs):
        """Обновление спрайта"""
        platforms = kwargs.get("platforms")
        check_points = kwargs.get("check_points")
        self.check_check_points(check_points)
        keys = pg.key.get_pressed()
        left = keys[pg.K_a]
        right = keys[pg.K_d]
        up = keys[pg.K_SPACE]
        run = keys[pg.K_LSHIFT]

        if up:
            if self.on_wall and not self.last_update_is_jump:
                if self.dir == 1 and left or self.dir == -1 and right or not (left or right):
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
            if run:
                self.xvel = -FAST_RUN_SPEED
            else:
                self.xvel = -MOVE_SPEED
            self.dir = -1

        if right:
            if run:
                self.xvel = FAST_RUN_SPEED
            else:
                self.xvel = MOVE_SPEED
            self.dir = 1

        if self.isFly:
            if self.on_wall:
                self.anim = anims[self.dir]['wall_slide']
            else:
                if self.yvel > 0:
                    self.anim = anims[self.dir]['fall']
                else:
                    self.anim = anims[self.dir]['jump']
        else:
            if run:
                self.anim = anims[self.dir]['fast_run']
            else:
                self.anim = anims[self.dir]['run']

        if not (left or right) and not self.isFly:
            self.xvel = 0
            self.anim = anims[self.dir]['idle']
            self.on_wall = False

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

        if self.xvel and self.yvel >= 0:
            self.on_wall = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

        self.wall_check(platforms)

        if self.on_wall:
            self.yvel = self.wall_slide_speed

        self.hit_box.y = self.rect.y + self.hit_box_distance
        if self.xvel and (left or right) or self.on_wall:
            if self.dir == -1:
                self.hit_box.left = self.rect.x + self.hit_box_distance
            else:
                self.hit_box.right = self.rect.right - self.hit_box_distance
        else:
            self.hit_box.center = self.rect.center

    def collide(self, xvel, yvel, platforms):
        """Проверяет на столкновение с платформами"""
        for p in platforms:
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
                    self.on_wall = False
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

    def check_check_points(self, check_points):
        """Проверяет на столкновение с финишем"""
        for check_point in check_points:
            if pg.sprite.collide_rect(check_point, self):
                pg.event.post(pg.event.Event(GAME_EVENT_TYPE, data={
                    "type": "get_finish"
                }))

    def wall_check(self, platforms):
        """Проверяет на соприкосновение со сценами"""
        if self.on_wall:
            self.on_wall = False
            p1, p2 = self.get_wall_points()
            is_p1, is_p2 = False, False
            for p in platforms:
                if p.rect.collidepoint(*p1):
                    is_p1 = True
                if p.rect.collidepoint(*p2):
                    is_p2 = True
            self.on_wall = is_p1 and is_p2
        return self.on_wall

    def get_wall_points(self):
        """Получает точки проверки для стен"""
        if self.dir == -1:
            return ((self.rect.left - self.wall_check_point_large_x, self.rect.y + self.wall_check_point_large_y),
                    (self.rect.left - self.wall_check_point_large_x, self.rect.bottom - self.wall_check_point_large_y))
        return ((self.rect.right + self.wall_check_point_large_x, self.rect.y + self.wall_check_point_large_y),
                (self.rect.right + self.wall_check_point_large_x, self.rect.bottom - self.wall_check_point_large_y))

