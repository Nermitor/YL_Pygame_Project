import pygame as pg

from ui.config import font, scale_factor


class UITimer(pg.sprite.Sprite):
    def __init__(self, screen_width, y=1):
        super().__init__()
        self.screen_width = screen_width
        self.y = y * scale_factor
        self.time = 0
        self.set_time_text()
        self.rect = self.image.get_rect(centerx=screen_width // 2)
        self.rect.y = y
        self.run = False

    def set_text(self, text):
        self.image = font.render(text, False, "white")

    @staticmethod
    def get_time_s_text(time_ms):
        time_s = time_ms // 1000
        hrs, mins, secs = time_s // 3600, time_s % 3600 // 60, time_s % 60
        if hrs:
            return f"{hrs}:{mins}:{secs}."
        return f"{mins}:{secs}"

    def set_time_text(self):
        self.set_text(self.get_time_s_text(self.time))

    def update(self, *args, **kwargs):
        if self.run:
            print(self.time)
            self.time += self.timer()
            self.set_time_text()
            self.rect = self.image.get_rect(centerx=self.screen_width // 2)
            self.rect.y = self.y

    def start(self):
        self.timer = pg.time.Clock().tick
        self.run = True

    def stop(self):
        self.run = False

    def stopstart(self):
        self.run = not self.run

    def reset(self):
        self.time = 0
