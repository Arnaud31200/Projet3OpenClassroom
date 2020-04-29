import pygame
from Level import*

class player(pygame.sprite.Sprite):
    def __init__(self, level, move):
        super().__init__()
        self.health = 1
        self.attack = 0
        self.move = move
        self.logo = pygame.transform.scale(pygame.image.load("ressource/MacGyver.png"),(20, 20))  
        self.rect = self.logo.get_rect()      
        self.rect.x = 0
        self.rect.y = 0
        self.level = level
    
    def move_right(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y][log_x + 1] != 1 :
            self.rect.x += self.move
    
    def move_left(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y][log_x - 1] != 1 :
            self.rect.x -= self.move

    def move_up(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y - 1][log_x] != 1 :
            self.rect.y -= self.move

    def move_down(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y + 1][log_x] != 1 :
            self.rect.y += self.move

class guardian(pygame.sprite.Sprite):
    def __init__(self, outx, outy):
        super().__init__()
        self.health = 1
        self.attack = 0
        self.logo = pygame.transform.scale(pygame.image.load("ressource/Gardien.png"),(20, 20))
        self.rect = self.logo.get_rect()
        self.rect.y = outy
        self.rect.x = outx