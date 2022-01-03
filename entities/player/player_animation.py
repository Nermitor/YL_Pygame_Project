from glob import glob

import pygame as pg
from pyganim import PygAnimation as Anim

from utils.jsonreader import JsonReader

reader = JsonReader("entities/player/config.json")["animations"]
default_size = 50, 37
scale_factor = reader['scale_factor']
new_size = (default_size[0] * scale_factor, default_size[1] * scale_factor)


def make_anims(frames):
    k = Anim(frames), Anim(frames)
    for i in k:
        i.scale(new_size)
    k[1].flip(True, False)
    return k


player_run_anim_right, player_run_anim_left = make_anims(
    [(img, reader['run_anim_delay']) for img in glob("entities/player/animations/adventurer-run-*.png")])

player_idle_anim_right, player_idle_anim_left = make_anims(
    [(img, reader["idle_anim_delay"]) for img in glob("entities/player/animations/adventurer-idle-*.png")])

player_fall_anim_right, player_fall_anim_left = make_anims(
    [(img, reader['fall_anim_delay']) for img in glob("entities/player/animations/adventurer-fall-*.png")])

player_die_anim_right, player_die_anim_left = make_anims(
    [(img, reader['die_anim_delay']) for img in glob("entities/player/animations/adventurer-die-*.png")])

player_items_anim_right, player_items_anim_left = make_anims(
    [(img, reader['items_anim_delay']) for img in glob("entities/player/animations/adventurer-items-*.png")])

player_wall_slide_anim_right, player_wall_slide_anim_left = make_anims(
    [(img, reader['wall_slide_anim_delay']) for img in glob("entities/player/animations/adventurer-wall-slide-*.png")])

player_jump_anim_right, player_jump_anim_left = make_anims(
    [("entities/player/animations/adventurer-jump-02.png", reader['jump_anim_delay'])])
