from ui.button import OnlyImageButton
from config.config_file import common_config
from utils.image import scalex
import pygame as pg
from userevents import *

scale_factor = common_config['common']['scale_factor'] * common_config['menu']['scale_factor']

image_folder = "ui/resources/Large Buttons/"


class ButtonFabric:
    def __new__(cls, image, call_back_function):
        class Button(OnlyImageButton):
            def __init__(self, x, y):
                super().__init__(x, y, image, call_back_function)
        return Button


start = ButtonFabric(pg.image.load(image_folder + "Start Button.png"),
                     generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                         "type": "button_click",
                         "button": "start"
                     }))
ext = ButtonFabric(pg.image.load(image_folder + "Exit Button.png"),
                   generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                       "type": "button_click",
                       "button": "exit"
                   }))


