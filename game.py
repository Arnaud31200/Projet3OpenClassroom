import pygame
from Level import*
from screen import*
from playerguardian import*
from items import*

class game:
    def __init__(self):
        self.SCREEN = screen(300, 300)
        self.LEVEL = level(Level1, self.SCREEN.sprite)
        self.PLAYER = player(self.LEVEL, self.SCREEN.sprite)
        self.GUARDIAN = guardian(self.LEVEL.guard_posx, self.LEVEL.guard_posy)
        self.ITEMS = items(self.LEVEL)
        self.AIGUILLE = aiguille()