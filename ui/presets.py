from ui.button import OnlyImageButton
from ui.config import *
from userevents import *

image_folder = "ui/resources/buttons/"


class ButtonFabric:
    def __new__(cls, image, call_back_function, scaling, **kwargs):
        class Button(OnlyImageButton):
            def __init__(self, x, y):
                super().__init__(x, y, image, call_back_function, scaling, **kwargs)

        return Button


menu_start = ButtonFabric(pg.image.load(image_folder + "Start Button.png"),
                          generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                              "type": "button_click",
                              "button": "menu_start"
                          }), scaling=big_menu_button_scale_factor, addictions=(True, False))
menu_exit = ButtonFabric(pg.image.load(image_folder + "Exit Button.png"),
                         generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                             "type": "button_click",
                             "button": "menu_exit"
                         }), scaling=big_menu_button_scale_factor, addictions=(True, False))
menu_music = ButtonFabric(pg.image.load(image_folder + "Music Square Button.png"),
                          generate_event_function(SOUND_MANAGER_EVENT_TYPE, data={
                              "type": "button_click",
                              "button": "menu_music"
                          }), scaling=small_menu_buttons_scale_factor)

game_pause = ButtonFabric(pg.image.load(image_folder + "Pause Square Button.png"),
                          generate_event_function(GAME_EVENT_TYPE, data={
                              "type": "button_click",
                              "button": "game_pause"
                          }), scaling=game_buttons_scale_factor)
