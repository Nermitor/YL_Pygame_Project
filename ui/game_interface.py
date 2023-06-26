"""Игровой таймер"""

import pygame as pg

from ui.config import timer_font, timer_scale_factor


class UITimer(pg.sprite.Sprite):
    def __init__(self, screen_width, y=1):
        """Инициализация"""
        super().__init__()
        self.screen_width = screen_width
        self.y = y * timer_scale_factor
        self.time = 0
        self.set_time_text()
        self.rect = self.image.get_rect(centerx=screen_width // 2)
        self.rect.y = y
        self.run = False

    def set_text(self, text):
        """Установка текста"""
        self.image = timer_font.render(text, False, "white")

    @staticmethod
    def get_time_s_text(time_ms):
        """Получение читаемого текста из количества милисекунд"""
        time_s = time_ms // 1000
        hrs, mins, secs = time_s // 3600, time_s % 3600 // 60, time_s % 60
        if hrs:
            return f"{hrs}:{mins}:{secs}."
        return f"{mins}:{secs}"

    def get_time(self):
        """Получение текущего времени в милисекундах"""
        return self.time

    def set_time_text(self):
        """Установка текста из текущего времени"""
        self.set_text(self.get_time_s_text(self.time))

    def update(self, *args, **kwargs):
        """Обновление"""
        if self.run:
            self.time += self.timer()
            self.set_time_text()
            self.rect = self.image.get_rect(centerx=self.screen_width // 2)
            self.rect.y = self.y


    def start(self):
        """Старт таймера"""
        self.timer = pg.time.Clock().tick
        self.run = True

    def stop(self):
        """Остановка таймера"""
        self.run = False

    def reset(self):
        """Сброс таймера"""
        self.time = 0

    def handle_event(self, *args, **kwargs):
        pass
