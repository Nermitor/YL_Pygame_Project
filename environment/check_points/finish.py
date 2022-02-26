"""Спрайт финиша"""

from environment.check_points.check_point import AbstractCheckPoint


class Finish(AbstractCheckPoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
