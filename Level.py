import pygame
from random import*

class screen:
    def __init__(self, width, height):
        self.title = pygame.display.set_caption("Mac Gayver")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprite = self.width / 15
        self.outx = self.width - self.sprite
        self.outy = self.height - self.sprite

class level:
    def __init__(self, level, sprite, screen):
        self.screen = screen
        self.LEVEL = level
        self.POSITION_ITEMS = []
        self.COORDONNEES = []
        self.sprite = sprite
        self.Floor = pygame.transform.scale(pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(0,160,20,20), (20, 20))
        self.Wall = pygame.transform.scale(pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(40,0,20,20), (20, 20))
        self.Start = pygame.transform.scale(pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(160,20,20,20), (20, 20))

    def pos_player(self):
        for list in self.LEVEL:
            for number in list :
                if number == 3:
                    player_posy = (self.LEVEL.index(list)) * self.sprite
                    player_posx = (list.index(number)) * self.sprite
        return player_posx, player_posy

    def pos_guardian(self):
        for list in self.LEVEL:
            for number in list :
                if number == 4:
                    guard_posy = (self.LEVEL.index(list)) * self.sprite
                    guard_posx = (list.index(number)) * self.sprite
        return guard_posx, guard_posy

    def draw(self):
        num_ligne = 0
        for ligne in self.LEVEL:
            num_case = 0
            for number in ligne:
                a = num_case * self.screen.sprite
                b = num_ligne * self.screen.sprite
                if number == 1:
                    self.screen.screen.blit(self.Wall, (a,b))
                elif number == 0:
                    self.screen.screen.blit(self.Floor, (a,b))
                elif number == 3 or number == 4:
                    self.screen.screen.blit(self.Start, (a,b))
                num_case += 1
            num_ligne += 1

    def from_coord_to_grid(self, posx, posy):
        x = max(0, int(posx / self.sprite))
        y = max(0, int(posy / self.sprite))
        return x, y

    def coorditems(self):
        for index_y, ordonnees in enumerate(self.LEVEL):
            for index_x, number in enumerate(ordonnees) :
                if number == 0:
                    self.POSITION_ITEMS.append((index_x * self.sprite, index_y * self.sprite))
        hasard = choice(self.POSITION_ITEMS)
        x = hasard[0]
        y = hasard[1]
        self.COORDONNEES.append((x, y))
        self.POSITION_ITEMS.remove(hasard)
        return x, y
    
Level1 = [
[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,4]]