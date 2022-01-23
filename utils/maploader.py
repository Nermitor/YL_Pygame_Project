import pygame as pg
import pytmx

from environment.platform.platform import Platform
from entities.player.player import Player


class Map:
    def __init__(self, map_file_name):
        self.map = pytmx.load_pygame(map_file_name)
        print(self.map.layers)
        self.height = self.map.height
        self.width = self.map.width
        self.tile_height = self.map.tileheight
        self.tile_width = self.map.tilewidth
        self.sprites = {
            "platforms": pg.sprite.Group(),
            "player": pg.sprite.Group()
        }
        self.bg = self.map.get_layer_by_name("bg").image

        self.init_sprites()

    def init_sprites(self):
        for tile_x in range(self.width):
            for tile_y in range(self.height):
                platform_image = self.map.get_tile_image(tile_x, tile_y, 0)
                if platform_image is not None:
                    self.sprites['platforms'].add(
                        Platform.from_tile_cords((tile_x, tile_y), (self.map.tilewidth, self.map.tileheight), platform_image)

                    )
                player_image = self.map.get_tile_image(tile_x, tile_y, 1)
                if player_image is not None:
                    self.sprites['player'].add(Player(tile_x * self.map.tilewidth, tile_y * self.map.tileheight))

    def get_sprite_groups(self):
        return self.sprites.values()

    def get_player(self):
        return self.sprites['player'].sprites()[0]

    def update(self):
        self.sprites['platforms'].update()
        self.sprites['player'].update(self.sprites['platforms'])

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        for sprite_group in self.get_sprite_groups():
            sprite_group.draw(screen)
