import pygame
from Level import*
from playerguardian import*

class screen:
    def __init__(self, width, height):
        self.title = pygame.display.set_caption("Mac Gayver")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprite = self.width / 15
        self.outx = self.width - self.sprite
        self.outy = self.height - self.sprite

class game:
    def __init__(self):
        self.SCREEN = screen(300, 300)
        self.LEVEL = level(Level1)
        self.GUARDIAN = guardian(self.SCREEN.outx, self.SCREEN.outy)
        self.PRESSED = {}
        self.PLAYER = player(self.LEVEL, self.SCREEN.sprite)
