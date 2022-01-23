import pygame as pg

from utils.jsonreader import JsonReader
from utils.maploader import Map
from entities.camera.camera import Camera




def main():
    pg.init()
    reader = JsonReader("common.json")
    screen_size = reader["screen_size"]
    screen = pg.display.set_mode(screen_size)

    game_map = Map("maps/tiles/безымянный.tmx")

    timer = pg.time.Clock()

    camera = Camera(*screen_size)

    running = True
    while running:
        timer.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


        screen.fill("black")
        game_map.update()
        camera.update(game_map.get_player())
        for group in game_map.sprites.values():
            for sprite in group:
                camera.apply(sprite)

        game_map.draw(screen)
        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    main()
