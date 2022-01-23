from utils.jsonreader import JsonReader

common = JsonReader('common.json')
player_physics = JsonReader("entities/player/physics/physics.json")
player_animations = JsonReader('entities/player/animations/animations.json')


common_scale_factor = common['scale_factor']
animations_scale_factor = player_animations['scale_factor']

total_scale_factor = common_scale_factor * animations_scale_factor

DEFAULT_DIR = player_physics['default_dir']
MOVE_SPEED = player_physics['move_speed'] * total_scale_factor
JUMP_POWER = player_physics['jump_power'] * total_scale_factor
GRAVITY = player_physics['gravity'] * total_scale_factor

