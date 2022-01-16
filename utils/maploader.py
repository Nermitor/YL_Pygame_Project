import pygame as pg
import pytmx

from environment.platform.platform import Platform


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
        s = 1
        for tile_x in range(self.width):
            for tile_y in range(self.height):
                image = self.map.get_tile_image(tile_x, tile_y, 0)
                if image is not None:
                    self.sprites['platforms'].add(
                        Platform(tile_x * self.tile_width * s, tile_y * self.tile_height * s,
                                 pg.transform.scale(image, (self.tile_width * s, self.tile_height * s)))
                    )

    def get_sprite_groups(self):
        return self.sprites.values()

    def update(self):
        self.sprites['platforms'].update()
        self.sprites['player'].update(self.sprites['platforms'])

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        for sprite_group in self.get_sprite_groups():
            sprite_group.draw(screen)
