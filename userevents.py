from functools import partial

import pygame as pg

GAME_EVENT_TYPE = pg.USEREVENT
MENU_EVENT_TYPE = pg.USEREVENT + 1
SCENE_AGGREGATOR_EVENT_TYPE = pg.USEREVENT + 2
SOUND_MANAGER_EVENT_TYPE = pg.USEREVENT + 3

QUIT_EVENT = pg.event.Event(pg.QUIT)


def generate_event(event, **kwargs):
    if (t := type(event)) is type(pg.QUIT):
        pg.event.post(pg.event.Event(event, **kwargs))
    elif t is pg.event.Event:
        pg.event.post(event)
    else:
        raise ValueError


def generate_event_function(event, **kwargs):
    return partial(generate_event, event, **kwargs)
