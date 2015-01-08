
import random

class Card:
    'Individual card info'
    card_list = []

    def __init__(self, x, y, icons):
        self.x = x
        self.y = y
        self.icon = icons[0][0]
        self.face_color = icons[0][1]
        self.rect = (0, 0, [0, 0, 0, 0])
        Card.card_list.append(self)