import pygame

class items(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level

class aiguille(items):
    def __init__(self):
        super().__init__()
        self.aiguille = pygame.transform.scale(pygame.image.load("ressource/aiguille.png"),(20, 20))
        self.rect = self.aiguille.get_rect()

class ether(items):
    def __init__(self):
        super().__init__()   
        self.ether = pygame.transform.scale(pygame.image.load("ressource/ether.png"),(20, 20))
        self.rect = self.ether.get_rect()

class seringue(items):
    def __init__(self):
        super().__init__()      
        self.seringue = pygame.transform.scale(pygame.image.load("ressource/seringue.png"),(20, 20))
        self.rect = self.seringue.get_rect()

class tube(items):
    def __init__(self):
        super().__init__()        
        self.tube = pygame.transform.scale(pygame.image.load("ressource/tube_plastique.png"),(20, 20))
        self.rect = self.tube.get_rect()