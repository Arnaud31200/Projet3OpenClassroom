import pygame
from random import*
from Level import*
from game import*

class items(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level

class aiguille(items):
    def __init__(self):
        super().__init__(level)
        self.aiguille = pygame.transform.scale(pygame.image.load("ressource/aiguille.png"),(20, 20))
        self.rect = self.aiguille.get_rect()
        i, j = self.level.randomcoord(self)
        self.rect.x = i
        self.rect.y = j

class ether(items):
    def __init__(self, posx, posy):
        super().__init__(level)   
        self.ether = pygame.transform.scale(pygame.image.load("ressource/ether.png"),(20, 20))
        self.rect = self.ether.get_rect()

class seringue(items):
    def __init__(self, posx, posy):
        super().__init__(level)      
        self.seringue = pygame.transform.scale(pygame.image.load("ressource/seringue.png"),(20, 20))
        self.rect = self.seringue.get_rect()

class tube(items):
    def __init__(self, posx, posy):
        super().__init__(level)        
        self.tube = pygame.transform.scale(pygame.image.load("ressource/tube_plastique.png"),(20, 20))
        self.rect = self.tube.get_rect()