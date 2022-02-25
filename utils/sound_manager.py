import pygame as pg


class SoundManager:
    def __init__(self):
        pg.mixer.music.load("sounds/background.mp3")
        self.music_played = True
        pg.mixer.music.play()

    def handle_event(self, event):
        data = event.data
        if data['type'] == "button_click":
            if data['button'] == "menu_music":
                self.music_played ^= 1
                self.set_music(self.music_played)

    @staticmethod
    def set_music(is_play):
        if is_play:
            pg.mixer.music.unpause()
        else:
            pg.mixer.music.pause()
