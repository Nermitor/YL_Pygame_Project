import pygame as pg

from config.config_file import common_config

pg.font.init()

common = common_config['common']
ui = common_config['gui']

scale_factor = ui['scale_factor'] * common["scale_factor"]

font_dir = 'ui/resources/fonts/'

font = pg.font.Font(f"{font_dir}{ui['font']}.ttf", ui['font_size'] * scale_factor)
