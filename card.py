
import random

class Card:
    'Individual card info'
    instances = []

    def __init__(self, x, y, icons):
        self.x = x
        self.y = y
        self.mode = 0
        self.icon = icons[0][0]
        self.highlight = (236, 240, 241)
        self.color = icons[0][1]
        self.rect = (0, 0, [0, 0, 0, 0])
        Card.instances.append(self)