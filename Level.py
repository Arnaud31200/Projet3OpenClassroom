"""Import Modules"""
from random import choice
import pygame

class Level:
    """Level config"""
    def __init__(self, sprite, screen):
        self.level = []
        self.items_cordinates_list= []
        self.random_items_cordinates = []
        with open("level1.txt", "r") as level_selected:
            for line in level_selected.readlines():
                linenumber = []
                for number in line:
                    if number != "\n":
                        linenumber.append(int(number.strip()))
                self.level.append(linenumber)
        self.screen = screen
        self.sprite = sprite
        self.floor = pygame.image.load(
            "ressource/floor-tiles-20x20.png").subsurface(180, 240, 20, 20)
        self.wall = pygame.image.load(
            "ressource/floor-tiles-20x20.png").subsurface(40, 140, 20, 20)

    def draw(self):
        """Set drawing labyrinth"""
        line_number = 0
        for line in self.level:
            grid_number = 0
            for number in line:
                posx = grid_number * self.screen.sprite
                posy = line_number * self.screen.sprite
                if number == 1:
                    self.screen.screen.blit(self.wall, (posx, posy))
                elif number in (0, 2, 3):
                    self.screen.screen.blit(self.floor, (posx, posy))
                grid_number += 1
            line_number += 1

    def from_cord_to_grid(self, absciss, ordinate):
        """Set cordinates for next grid"""
        posx = max(0, int(absciss / self.sprite))
        posy = max(0, int(ordinate / self.sprite))
        return posx, posy

    def player_cord(self):
        """Set player cordinates"""
        for line in self.level:
            for number in line:
                if number == 2:
                    player_posy = (self.level.index(line)) * self.sprite
                    player_posx = (line.index(number)) * self.sprite
        return player_posx, player_posy

    def guardian_cord(self):
        """Set guardian cordinates"""
        for line in self.level:
            for number in line:
                if number == 3:
                    guard_posy = (self.level.index(line)) * self.sprite
                    guard_posx = (line.index(number)) * self.sprite
        return guard_posx, guard_posy

    def items_cord(self):
        """Set items cordinates"""
        for index_y, ordinates in enumerate(self.level):
            for index_x, number in enumerate(ordinates):
                if number == 0:
                    self.items_cordinates_list.append((index_x * self.sprite, index_y * self.sprite))

    def random_cord(self):
        """ Set Random cordinates for items"""
        random_coord = choice(self.items_cordinates_list)
        posx = random_coord[0]
        posy = random_coord[1]
        self.random_items_cordinates.append((posx, posy))
        self.items_cordinates_list.remove(random_coord)
        return posx, posy
