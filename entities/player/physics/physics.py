"""Физические константы"""

from config.config import config

player = config['entities']['player']
player_physics = player['physics']
player_animations = player['animations']

common_scale_factor = config['common']['scale_factor']
animations_scale_factor = player_animations['scale_factor']

total_scale_factor = common_scale_factor * animations_scale_factor

DEFAULT_DIR = player_physics['default_dir']
MOVE_SPEED = player_physics['move_speed'] * total_scale_factor
JUMP_POWER = player_physics['jump_power'] * total_scale_factor
GRAVITY = player_physics['gravity'] * total_scale_factor
FAST_RUN_SPEED = player_physics['fast_run_speed'] * total_scale_factor


def totalize(x):
    return total_scale_factor * x
