"""Import Modules"""
import pygame
from random import choice

Level1 = []
with open("level1.txt", "r") as f:
    for line in f.readlines():
        linenumber = []
        for number in line :
            if number != "\n":
                linenumber.append(int(number.strip()))
        Level1.append(linenumber)

class Level:
    """Level config"""
    def __init__(self, level, sprite, screen):
        self.screen = screen
        self.level = level
        self.items_position = []
        self.coordinates = []
        self.sprite = 20
        self.floor = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(180, 240, 20, 20)
        self.wall = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(40, 140, 20, 20)

    def pos_player(self):
        """Set player position"""
        for line in self.level:
            for number in line:
                if number == 3:
                    player_posy = (self.level.index(line)) * self.sprite
                    player_posx = (line.index(number)) * self.sprite
        return player_posx, player_posy

    def pos_guardian(self):
        """Set guardian position"""
        for line in self.level:
            for number in line:
                if number == 4:
                    guard_posy = (self.level.index(line)) * self.sprite
                    guard_posx = (line.index(number)) * self.sprite
        return guard_posx, guard_posy

    def draw(self):
        """Set drawing labyrinth"""
        line_number = 0
        for line in self.level:
            grid_number = 0
            for number in line:
                X = grid_number * self.screen.sprite
                Y = line_number * self.screen.sprite
                if number == 1:
                    self.screen.screen.blit(self.wall, (X, Y))
                elif number == 0 or number == 3 or number == 4:
                    self.screen.screen.blit(self.floor, (X, Y))
                grid_number += 1
            line_number += 1

    """Set cordinates for next grid"""
    def from_cord_to_grid(self, posx, posy):
        X = max(0, int(posx / self.sprite))
        Y = max(0, int(posy / self.sprite))
        return X, Y

    """Set items cordinates"""
    def items_cord(self):
        for index_y, ordinates in enumerate(self.level):
            for index_x, number in enumerate(ordinates):
                if number == 0:
                    self.items_position.append((index_x * self.sprite, index_y * self.sprite))
        
    def random_cord(self):
        random_coord = choice(self.items_position)
        X = random_coord[0]
        Y = random_coord[1]
        self.coordinates.append((X, Y))
        self.items_position.remove(random_coord)
        return X, Y
