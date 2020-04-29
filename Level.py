import pygame

class level:
    def __init__(self, level):
        self.LEVEL = level
        self.Floor = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(0,160,20,20)
        self.Wall = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(40,0,20,20)
        self.Start = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(160,20,20,20)

    def from_coord_to_grid(self, posx, posy):
        i = max(0, int(posx / 20))
        j = max(0, int(posy / 20))
        return i, j


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