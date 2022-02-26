"""Возвращает список доступных уровней"""

import os.path as path
from itertools import count

from utils.jsonio import JsonIO


def get_levels(get_path=False):
    levels = []
    for level_num in count(1):
        if pth := path.exists(f"maps/tiles/{level_num}.tmx"):
            if get_path:
                levels.append(pth)
            else:
                levels.append(level_num)
        else:
            break
    data = JsonIO("config/temp.json")
    data['max_level'] = max(levels)
    return levels
