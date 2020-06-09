"""Import Modules"""
import pygame
from Level import Level

class Items(pygame.sprite.Sprite):
    """Items config"""
    def __init__(self, level, logo, player):
        super().__init__()
        self.player = player
        self.level = level
        self.logo = pygame.transform.scale(pygame.image.load(logo), (20, 20))
        self.rect = self.logo.get_rect()
        X, Y = self.level.random_cord()
        self.rect.x = X
        self.rect.y = Y

class Player(pygame.sprite.Sprite):
    """Player config"""
    def __init__(self, level, move, screen, guardian):
        self.guardian = guardian
        self.screen = screen
        self.level = level
        self.health = 1
        self.attack = 0
        self.move = move
        self.logo = pygame.transform.scale(pygame.image.load("ressource/MacGyver.png"), (20, 20))
        self.rect = self.logo.get_rect()
        X, Y = self.level.pos_player()
        self.rect.x = X
        self.rect.y = Y

    def health_attack_up(self):
        """Set health and attack up"""
        self.health = self.health + 1
        self.attack = self.attack + 1

    """Set player movements"""
    def move_right(self):
        log_x, log_y = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_y][log_x + 1] != 1:
            self.screen.screen.blit(self.level.floor, (self.rect.x, self.rect.y))
            self.rect.x += self.move
            self.screen.screen.blit(self.logo, self.rect)

    def move_left(self):
        log_x, log_y = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_y][log_x - 1] != 1:
            self.screen.screen.blit(self.level.floor, (self.rect.x, self.rect.y))
            self.rect.x -= self.move
            self.screen.screen.blit(self.logo, self.rect)

    def move_up(self):
        log_x, log_y = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_y - 1][log_x] != 1:
            self.screen.screen.blit(self.level.floor, (self.rect.x, self.rect.y))
            self.rect.y -= self.move
            self.screen.screen.blit(self.logo, self.rect)

    def move_down(self):
        log_x, log_y = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_y + 1][log_x] != 1:
            self.screen.screen.blit(self.level.floor, (self.rect.x, self.rect.y))
            self.rect.y += self.move
            self.screen.screen.blit(self.logo, self.rect)

class Guardian(pygame.sprite.Sprite):
    """Guardian config"""
    def __init__(self, level):
        self.level = level
        self.health = 4
        self.attack = 4
        self.logo = pygame.transform.scale(pygame.image.load("ressource/Gardien.png"), (20, 20))
        self.rect = self.logo.get_rect()
        x, y = self.level.pos_guardian()
        self.rect.x = x
        self.rect.y = y
