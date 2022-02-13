from abc import ABC, abstractmethod


class MetaScene(ABC):

    @abstractmethod
    def set(self, *args, **kwargs):
        ...

    @abstractmethod
    def unset(self):
        ...

    @abstractmethod
    def draw(self, screen):
        ...

    @abstractmethod
    def update(self, *args, **kwargs):
        ...

    @abstractmethod
    def handle_event(self, event):
        ...
