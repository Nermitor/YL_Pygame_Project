import pygame as pg

from config.config_file import common_config
from scenes.scene_aggregator import SceneAggregator


def main():
    pg.init()
    screen = pg.display.set_mode(common_config['common']['screen_size'])

    scene_aggregator = SceneAggregator()
    scene_aggregator.switch_to("menu")

    fps = common_config['common']['fps']
    clock = pg.time.Clock()

    running = True
    while running:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            else:
                scene_aggregator.handle_event(event)

        scene_aggregator.update_cur_scene()
        scene_aggregator.draw_cur_scene(screen)

        pg.display.update()


if __name__ == "__main__":
    main()
