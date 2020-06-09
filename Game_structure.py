"""Import Modules"""
import pygame
from Sprites import Player
from Sprites import Items
from Sprites import Guardian
from Level import Level
from Level import Level1

class Screen:
    """Screen config"""
    def __init__(self, width, height):
        self.title = pygame.display.set_caption("Mac Gayver")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprite = self.width / 15
        self.outx = self.width - self.sprite
        self.outy = self.height - self.sprite

class Game:
    """Game config"""
    def __init__(self):
        self.SCREEN = Screen(300, 300)
        self.LEVEL = Level(Level1, self.SCREEN.sprite, self.SCREEN)
        self.LEVEL.items_cord()
        self.GUARDIAN = Guardian(self.LEVEL)
        self.PLAYER = Player(self.LEVEL, self.SCREEN.sprite, self.SCREEN, self.GUARDIAN)
        self.NEEDLE = Items(self.LEVEL, "ressource/aiguille.png", self.PLAYER)
        self.ETHER = Items(self.LEVEL, "ressource/ether.png", self.PLAYER)
        self.SYRINGUE = Items(self.LEVEL, "ressource/seringue.png", self.PLAYER)
        self.PIPE = Items(self.LEVEL, "ressource/tube_plastique.png", self.PLAYER)

    def collect_items(self):
        """Set items collection by player"""
        if self.PLAYER.rect == self.NEEDLE.rect:
            self.PLAYER.health_attack_up()
        elif self.PLAYER.rect == self.ETHER.rect:
            self.PLAYER.health_attack_up()
        elif self.PLAYER.rect == self.SYRINGUE.rect:
            self.PLAYER.health_attack_up()
        elif self.PLAYER.rect == self.PIPE.rect:
            self.PLAYER.health_attack_up()

    def guardian_collide(self):
        """Set player behavior against guardian"""
        log_x, log_y = self.LEVEL.from_cord_to_grid(self.PLAYER.rect.x, self.PLAYER.rect.y)
        if self.LEVEL.level[log_y][log_x] == 4:
            self.PLAYER.health = self.PLAYER.health - self.GUARDIAN.attack
            self.GUARDIAN.health = self.GUARDIAN.health - self.PLAYER.attack
