"""Import Modules"""
import pygame
from Sprites import Player
from Sprites import Items
from Sprites import Guardian
from Level import Level
from Level import Level1

class Screen:
    """Screen config"""
    def __init__(self, width, height, sprite):
        self.title = pygame.display.set_caption("Mac Gayver")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprite = sprite
        self.outx = self.width - self.sprite
        self.outy = self.height - self.sprite

class Game:
    """Game config"""
    def __init__(self):
        self.screen = Screen(300, 300, 20)
        self.level = Level(Level1, self.screen.sprite, self.screen)
        self.level.items_cord()
        self.guardian = Guardian(self.level)
        self.player = Player(self.level, self.screen.sprite, self.screen, self.guardian)
        self.needle = Items(self.level, "ressource/aiguille.png", self.player)
        self.ether = Items(self.level, "ressource/ether.png", self.player)
        self.syringue = Items(self.level, "ressource/seringue.png", self.player)
        self.pipe = Items(self.level, "ressource/tube_plastique.png", self.player)

    def collect_items(self):
        """Set items collection by player"""
        if self.player.rect == self.needle.rect:
            self.player.health_attack_up()
        elif self.player.rect == self.ether.rect:
            self.player.health_attack_up()
        elif self.player.rect == self.syringue.rect:
            self.player.health_attack_up()
        elif self.player.rect == self.pipe.rect:
            self.player.health_attack_up()

    def guardian_collide(self):
        """Set player behavior against guardian"""
        log_x, log_y = self.level.from_cord_to_grid(self.player.rect.x, self.player.rect.y)
        if self.level.level[log_y][log_x] == 4:
            self.player.health = self.player.health - self.guardian.attack
            self.guardian.health = self.guardian.health - self.player.attack
