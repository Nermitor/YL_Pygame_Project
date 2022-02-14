import pygame as pg
from functools import partial

GAME_EVENT_TYPE = pg.USEREVENT
GET_FINISH_EVENT = pg.event.Event(GAME_EVENT_TYPE, event="get_finish")

MENU_EVENT_TYPE = pg.USEREVENT + 1

SCENE_AGGREGATOR_EVENT_TYPE = pg.USEREVENT + 2

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