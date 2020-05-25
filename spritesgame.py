import pygame
from Level import*

class player(pygame.sprite.Sprite):
    def __init__(self, level, move):
        self.level = level
        self.health = 4
        self.attack = 4
        self.move = move
        self.logo = pygame.transform.scale(pygame.image.load("ressource/MacGyver.png"),(20, 20))  
        self.rect = self.logo.get_rect()
        x, y = self.level.pos_player()
        self.rect.x = x
        self.rect.y = y

    def draw_move(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y][log_x + 1] == 0 :
            self.level.Floor

    def move_right(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y][log_x + 1] != 1 :
            self.draw_move()
            self.rect.x += self.move

    def move_left(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y][log_x - 1] != 1 :
            self.draw_move()
            self.rect.x -= self.move

    def move_up(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y - 1][log_x] != 1 :
            self.draw_move()
            self.rect.y -= self.move

    def move_down(self):
        log_x, log_y = self.level.from_coord_to_grid(self.rect.x, self.rect.y)
        if self.level.LEVEL[log_y + 1][log_x] != 1 :
            self.draw_move()
            self.rect.y += self.move

class guardian(pygame.sprite.Sprite):
    def __init__(self, level):
        self.level = level
        self.health = 4
        self.attack = 4
        self.logo = pygame.transform.scale(pygame.image.load("ressource/Gardien.png"),(20, 20))
        self.rect = self.logo.get_rect()
        x, y = self.level.pos_guardian()
        self.rect.x = x
        self.rect.y = y

class items(pygame.sprite.Sprite):
    def __init__(self, level, logo):
        super().__init__()
        self.level = level
        self.logo = pygame.transform.scale(pygame.image.load(logo),(20, 20))
        self.rect = self.logo.get_rect()
        i, j = self.level.coorditems()
        self.rect.x = i
        self.rect.y = j