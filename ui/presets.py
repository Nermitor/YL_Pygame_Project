from ui.button import OnlyImageButton
from ui.config import *
from userevents import *

image_folder = "ui/resources/buttons/"


class ButtonFabric:
    def __new__(cls, image, call_back_function, scaling=None, **kwargs):
        class Button(OnlyImageButton):
            def __init__(self, x, y, init_scaling=None, **init_kwargs):
                sc = init_scaling if init_scaling is not None else scaling
                super().__init__(x, y, image, call_back_function, sc, **kwargs | init_kwargs)

        return Button


class DifficultCallBackButtonsFabric:
    def __new__(cls, image, scaling=None, **kwargs):
        class Button(OnlyImageButton):
            def __init__(self, x, y, call_back_function, init_scaling=None, **init_kwargs):
                sc = init_scaling if init_scaling is not None else scaling
                super().__init__(x, y, image, call_back_function, sc, **kwargs | init_kwargs)

        return Button


menu_start = ButtonFabric(pg.image.load(image_folder + "Start Button.png"),
                          generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                              "type": "switch_scene",
                              "scene": "game"
                          }), scaling=big_menu_button_scale_factor, addictions=(True, False))
menu_exit = ButtonFabric(pg.image.load(image_folder + "Exit Button.png"),
                         generate_event_function(pg.QUIT), scaling=big_menu_button_scale_factor,
                         addictions=(True, False))
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

game_play = ButtonFabric(pg.image.load(image_folder + "Play Square Button.png"),
                         generate_event_function(GAME_EVENT_TYPE, data={
                             "type": "button_click",
                             "button": "game_play"
                         }))

game_home = ButtonFabric(pg.image.load(image_folder + "Home Square Button.png"),
                         generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                             "type": "switch_scene",
                             "scene": "menu"
                         }))
game_reset = ButtonFabric(pg.image.load(image_folder + "Return Square Button.png"),
                          generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                              "type": "switch_scene",
                              "scene": "game"
                          }))
game_next_level = ButtonFabric(pg.image.load(image_folder + "Next Square Button.png"),
                               generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                                   "type": "next_game_level"
                               }))
menu_levels = ButtonFabric(pg.image.load(image_folder + "Levels Square Button.png"),
                           generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                               "type": "switch_scene",
                               "scene": "levels"
                           }), scaling=small_menu_buttons_scale_factor)

menu_back = ButtonFabric(pg.image.load(image_folder + "Back Square Button.png"),
                         generate_event_function(SCENE_AGGREGATOR_EVENT_TYPE, data={
                             "type": "switch_scene",
                             "scene": "menu"
                         }), scaling=small_menu_buttons_scale_factor)

empty_button = DifficultCallBackButtonsFabric(pg.image.load(image_folder + "Empty Square Button.png"),
                                              scaling=small_menu_buttons_scale_factor)
