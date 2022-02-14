import pygame as pg


class AbstractButton(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, call_back_function: callable):
        super().__init__()
        self.call_back_function = call_back_function
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y

    def update(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(*event.pos):
                self.call_back_function()

    def handle_event(self, event):
        self.update(event)


class AbstractTextWithImageButton(AbstractButton):
    def __init__(self, x: int, y: int, text: str,
                 font: pg.font.Font, color: pg.Color, call_back_function: callable):
        self.text = font.render(text, False, color)
        self.image.blit(self.text, self.text.get_rect(center=(self.image.get_width() / 2, self.image.get_height() / 2)))
        super().__init__(x, y, call_back_function)
