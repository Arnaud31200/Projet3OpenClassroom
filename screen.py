import pygame

class screen:
    def __init__(self, width, height):
        self.title = pygame.display.set_caption("Mac Gayver")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprite = self.width / 15
        self.outx = self.width - self.sprite
        self.outy = self.height - self.sprite
