"""Абстрактный класс сцены"""

from abc import ABC, abstractmethod


class MetaScene(ABC):
    """Родитель для всех сцен"""
    def set(self, *args, **kwargs):
        """Инициализация сцены перед её установкой"""
        ...

    def unset(self):
        """Деинициализация сцены перед её сменой на другую"""
        ...

    @abstractmethod
    def draw(self, screen):
        """Отрисовка сцены на экран"""
        ...

    def update(self, *args, **kwargs):
        """Обновление сцены"""
        ...

    @abstractmethod
    def handle_event(self, event):
        """Обработка событий"""
        ...
