import pygame as pg

GAME_EVENT_TYPE = pg.USEREVENT

GET_FINISH_EVENT = pg.event.Event(GAME_EVENT_TYPE, event="get_finish")
QUIT_EVENT = pg.event.Event(pg.QUIT)
