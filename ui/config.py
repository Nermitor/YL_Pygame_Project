import pygame as pg

from config.config_file import common_config

pg.font.init()

common = common_config['common']

menu = common_config['menu']
menu_buttons = menu['buttons']

ui = common_config['gui']
game_buttons = ui['buttons']
timer = ui['timer']

common_scale_factor = common['scale_factor']
timer_scale_factor = ui['timer']['scale_factor'] * common_scale_factor
font_dir = 'ui/resources/fonts/'
timer_font = pg.font.Font(f"{font_dir}{timer['font']}.ttf", timer['font_size'] * timer_scale_factor)
game_buttons_scale_factor = common_scale_factor * game_buttons['scale_factor']
big_menu_button_scale_factor = menu_buttons['big_buttons']['scale_factor'] * common_scale_factor
small_menu_buttons_scale_factor = menu_buttons['small_buttons']['scale_factor'] * common_scale_factor

del common, menu, menu_buttons, ui, game_buttons, timer, common_config, pg
