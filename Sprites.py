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
        posx, posy = self.level.random_cord()
        self.rect.x = posx
        self.rect.y = posy

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
        posx, posy = self.level.player_cord()
        self.rect.x = posx
        self.rect.y = posy

    def health_attack_up(self):
        """Set health and attack up"""
        self.health = self.health + 1
        self.attack = self.attack + 1

    def move_right(self):
        """Set player movements"""
        log_posx, log_posy = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_posy][log_posx + 1] != 1:
            self.screen.screen.blit(self.level.floor, (self.rect.x, self.rect.y))
            self.rect.x += self.move
            self.screen.screen.blit(self.logo, self.rect)

    def move_left(self):
        """Set player movements"""
        log_posx, log_posy = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_posy][log_posx - 1] != 1:
            self.screen.screen.blit(self.level.floor, (self.rect.x, self.rect.y))
            self.rect.x -= self.move
            self.screen.screen.blit(self.logo, self.rect)

    def move_up(self):
        """Set Player movements"""
        log_posx, log_posy = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_posy - 1][log_posx] != 1:
            self.screen.screen.blit(self.level.floor, (self.rect.x, self.rect.y))
            self.rect.y -= self.move
            self.screen.screen.blit(self.logo, self.rect)

    def move_down(self):
        """Set player movements"""
        log_posx, log_posy = self.level.from_cord_to_grid(self.rect.x, self.rect.y)
        if self.level.level[log_posy + 1][log_posx] != 1:
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
        posx, posy = self.level.guardian_cord()
        self.rect.x = posx
        self.rect.y = posy
