"""Загрузчик уровней"""

import pygame as pg
import pytmx

from entities.player.player import Player
from environment.check_points import finish
from environment.platforms.platform import Platform


class Map:
    """Загружает карту из файла"""
    def __init__(self, map_file_name):
        self.map = pytmx.load_pygame(map_file_name)
        self.height = self.map.height
        self.width = self.map.width
        self.tile_height = self.map.tileheight
        self.tile_width = self.map.tilewidth
        self.sprites = {
            "platforms": pg.sprite.Group(),
            "player_group": pg.sprite.Group(),
            "check_points_group": pg.sprite.Group()
        }
        self.bg = self.map.get_layer_by_name("bg").image

        self.init_sprites()

    def init_sprites(self):
        """Инициализация всех спрйтов"""
        a = self.map.layernames["platforms"]

        for tile_x in range(self.width):
            for tile_y in range(self.height):
                platform_image = self.map.get_tile_image(tile_x, tile_y, 1)
                if platform_image is not None:
                    self.sprites['platforms'].add(
                        Platform.from_tile_cords((tile_x, tile_y), (self.map.tilewidth, self.map.tileheight),
                                                 platform_image)

                    )
                player_image = self.map.get_tile_image(tile_x, tile_y, 0)
                if player_image is not None:
                    self.sprites['player_group'].add(Player(tile_x * self.map.tilewidth, tile_y * self.map.tileheight))

                finish_image = self.map.get_tile_image(tile_x, tile_y, 3)
                if finish_image is not None:
                    self.sprites['check_points_group'].add(
                        finish.Finish.from_tile_cords((tile_x, tile_y), (self.map.tilewidth, self.map.tileheight),
                                                      finish_image))

    def get_sprite_groups(self):
        """Получение групп спрайтов"""
        return self.sprites.values()

    def get_player(self):
        """Получение спрайтов игрока"""
        return self.sprites['player_group'].sprites()[0]

    def get_bg(self):
        """Получение изображения заднего фона"""
        return self.bg

