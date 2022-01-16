from glob import glob
import pygame as pg

from pyganim import PygAnimation as Anim

from utils.jsonreader import JsonReader

reader = JsonReader("entities/player/animations/config.json")["animations"]
asset_folder = "entities/player/animations/assets/"
default_size = 26, 35
scale_factor = reader['scale_factor']
new_size = (default_size[0] * scale_factor, default_size[1] * scale_factor)


def make_anims(frames):
    k = Anim(frames), Anim(frames)
    for i in k:
        i.scale(new_size)
        i.set_colorkey((0, 0, 0))
    k[1].flip(True, False)
    return k


player_run_anim_right, player_run_anim_left = make_anims(
    [(img, reader['run_anim_delay']) for img in glob(f"{asset_folder}adventurer-run-*.png")])

player_idle_anim_right, player_idle_anim_left = make_anims(
    [(img, reader["idle_anim_delay"]) for img in glob(f"{asset_folder}adventurer-idle-*.png")])

player_fall_anim_right, player_fall_anim_left = make_anims(
    [(img, reader['fall_anim_delay']) for img in glob(f"{asset_folder}adventurer-fall-*.png")])

player_die_anim_right, player_die_anim_left = make_anims(
    [(img, reader['die_anim_delay']) for img in glob(f"{asset_folder}adventurer-die-*.png")])

player_items_anim_right, player_items_anim_left = make_anims(
    [(img, reader['items_anim_delay']) for img in glob(f"{asset_folder}adventurer-items-*.png")])

player_wall_slide_anim_right, player_wall_slide_anim_left = make_anims(
    [(img, reader['wall_slide_anim_delay']) for img in glob(f"{asset_folder}adventurer-wall-slide-*.png")])

player_jump_anim_right, player_jump_anim_left = make_anims(
    [(f"{asset_folder}adventurer-jump-02.png", reader['jump_anim_delay'])])

anims = {
    1: {
        "idle": player_idle_anim_right,
        "run": player_run_anim_right,
        "jump": player_jump_anim_right,
        "fall": player_fall_anim_right
    },
    -1: {
        "idle": player_idle_anim_left,
        "run": player_run_anim_left,
        "jump": player_jump_anim_left,
        "fall": player_fall_anim_left
    }
}
