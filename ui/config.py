import pygame as pg

from config.config_file import common_config

pg.font.init()

common = common_config['common']

menu = common_config['menu']
menu_buttons = menu['buttons']

ui = common_config['gui']
game_buttons = ui['buttons']
timer = ui['timer']
pause_menu = ui["pause_menu"]

common_scale_factor = common['scale_factor']
timer_scale_factor = ui['timer']['scale_factor'] * common_scale_factor
font_dir = 'ui/resources/fonts/'
timer_font = pg.font.Font(f"{font_dir}{timer['font']}.ttf", timer['font_size'] * timer_scale_factor)
game_buttons_scale_factor = common_scale_factor * game_buttons['scale_factor']
big_menu_button_scale_factor = menu_buttons['big_buttons']['scale_factor'] * common_scale_factor
small_menu_buttons_scale_factor = menu_buttons['small_buttons']['scale_factor'] * common_scale_factor
common_pause_menu_scale_factor = pause_menu['common']['scale_factor'] * common_scale_factor
buttons_pause_menu_scale_factor = pause_menu['buttons']['scale_factor'] * common_pause_menu_scale_factor
pause_menu_font = pg.font.Font(f"{font_dir}{pause_menu['text']['font']}.ttf", pause_menu['text']['font_size'])

del common, menu, menu_buttons, ui, game_buttons, timer, common_config, pg
