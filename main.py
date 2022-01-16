import pygame as pg

from entities.player.player import Player
from utils.jsonreader import JsonReader
from utils.maploader import Map


def main():
    pg.init()
    reader = JsonReader("config.json")
    screen_size = reader["screen_size"]
    screen = pg.display.set_mode(screen_size)

    game_map = Map("maps/tiles/безымянный.tmx")

    player = Player(300, 0)
    game_map.sprites['player'].add(player)

    timer = pg.time.Clock()

    running = True
    while running:
        timer.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill("black")
        game_map.update()
        game_map.draw(screen)

        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    main()
