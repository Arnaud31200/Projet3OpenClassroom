import pygame
from screen import*
from random import*

class level:
    def __init__(self, level, sprite):
        self.LEVEL = level
        self.POSITION_ITEMS = []
        self.sprite = sprite
        self.Floor = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(0,160,20,20)
        self.Wall = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(40,0,20,20)
        self.Start = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(160,20,20,20)
        for list in self.LEVEL:
            for number in list :
                if number == 4:
                    guard_posy = (self.LEVEL.index(list)) * self.sprite 
                    guard_posx = (list.index(number)) * self.sprite 
                elif number == 5:
                    posy = self.LEVEL.index(list) 
                    posx = list.index(number)
                    self.POSITION_ITEMS.append([posx * self.sprite, posy * self.sprite])
                elif number == 6:
                    posy = self.LEVEL.index(list) 
                    posx = list.index(number)
                    self.POSITION_ITEMS.append([posx * self.sprite, posy * self.sprite])
                elif number == 7:
                    posy = self.LEVEL.index(list) 
                    posx = list.index(number)
                    self.POSITION_ITEMS.append([posx * self.sprite, posy * self.sprite])
                elif number == 8:
                    posy = self.LEVEL.index(list) 
                    posx = list.index(number)
                    self.POSITION_ITEMS.append([posx * self.sprite, posy * self.sprite])               
        self.guard_posy = guard_posy
        self.guard_posx = guard_posx

    def randomcoord(self):
        randcoord = choice(self.POSITION_ITEMS)
        i = randcoord[0]
        j = randcoord[1]
        return i, j

    def from_coord_to_grid(self, posx, posy):
        x = max(0, int(posx / self.sprite))
        y = max(0, int(posy / self.sprite))
        return x, y

Level1 = [
[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[7,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,4]]