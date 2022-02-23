import pygame as pg

from scenes.metascene import MetaScene
from ui.presets import game_play, game_home, game_reset
from userevents import GAME_EVENT_TYPE
from ui.config import *
from utils.image import scalex
from ui.button import OnlyImageButton


class PauseMenu(MetaScene):
    def __init__(self, x, buttons_y, parent):
        self.cords = [x, buttons_y]

        self.parent = parent

        self.image = scalex(pg.image.load("ui/resources/menu_sheet.png"), common_pause_menu_scale_factor).convert()
        self.image.set_colorkey(pg.Color("white"))
        self.cords[0] -= self.image.get_width() // 2

        buttons_y = 350 * common_pause_menu_scale_factor
        self.resume_btn = game_play(self.image.get_width() // 2, buttons_y,
                                    init_scaling=buttons_pause_menu_scale_factor,
                                    addictions=(True, False))
        self.home_btn = game_home(self.image.get_width() // 2 + 100 * common_pause_menu_scale_factor, buttons_y,
                                  init_scaling=buttons_pause_menu_scale_factor,
                                  addictions=(True, False))
        self.reset_btn = game_reset(self.image.get_width() // 2 - 100 * common_pause_menu_scale_factor, buttons_y,
                                    init_scaling=buttons_pause_menu_scale_factor,
                                    addictions=(True, False))
        self.widgets = pg.sprite.Group(self.resume_btn, self.home_btn, self.reset_btn)
        self.text = pg.sprite.Sprite(self.widgets)
        self.text.image = scalex(pause_menu_font.render("Игра остановлена", False, pg.Color("white")),
                                 common_pause_menu_scale_factor)
        self.text.rect = self.text.image.get_rect()
        self.text.rect.x, self.text.rect.y = 50, 20

        self.init_widgets()

    def draw(self, screen):
        screen.blit(self.image, self.cords)
        self.widgets.draw(screen)

    def update(self, *args, **kwargs):
        pass

    def init_widgets(self):
        for widget in self.widgets:
            widget.rect.x += self.cords[0]
            widget.rect.y += self.cords[1]

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:

            for widget in self.widgets:
                if isinstance(widget, OnlyImageButton):
                    widget.handle_event(event)
        elif event.type == GAME_EVENT_TYPE:
            data = event.data
            if data['type'] == "button_click":
                if data['button'] == "game_play":
                    self.parent.frieze_scene(False)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.parent.frieze_scene(False)
