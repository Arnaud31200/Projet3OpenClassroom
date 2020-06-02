"""Import Modules"""
from random import choice
import pygame
pygame.init()

Level1 = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]]

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

class Level:
    """Level config"""
    def __init__(self, level, sprite, screen):
        self.screen = screen
        self.level = level
        self.items_position = []
        self.coordinates = []
        self.sprite = sprite
        self.floor = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(0, 160, 20, 20)
        self.wall = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(40, 0, 20, 20)

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
        x = max(0, int(posx / self.sprite))
        y = max(0, int(posy / self.sprite))
        return x, y

    """Set items cordinates"""
    def items_cord(self):
        for index_y, ordinates in enumerate(self.level):
            for index_x, number in enumerate(ordinates):
                if number == 0:
                    self.items_position.append((index_x * self.sprite, index_y * self.sprite))
        random_coord = choice(self.items_position)
        X = random_coord[0]
        Y = random_coord[1]
        self.coordinates.append((X, Y))
        self.items_position.remove(random_coord)
        return X, Y

class Items(pygame.sprite.Sprite):
    """Items config"""
    def __init__(self, level, logo, player):
        super().__init__()
        self.player = player
        self.level = level
        self.logo = pygame.transform.scale(pygame.image.load(logo), (20, 20))
        self.rect = self.logo.get_rect()
        X, Y = self.level.items_cord()
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

class Game:
    """Game config"""
    def __init__(self):
        self.SCREEN = Screen(300, 300)
        self.LEVEL = Level(Level1, self.SCREEN.sprite, self.SCREEN)
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

"""Game initialization"""
GAME = Game()
GAME.LEVEL.draw()
GAME.SCREEN.screen.blit(GAME.PLAYER.logo, GAME.PLAYER.rect)
GAME.SCREEN.screen.blit(GAME.GUARDIAN.logo, GAME.GUARDIAN.rect)
GAME.SCREEN.screen.blit(GAME.NEEDLE.logo, GAME.NEEDLE.rect)
GAME.SCREEN.screen.blit(GAME.ETHER.logo, GAME.ETHER.rect)
GAME.SCREEN.screen.blit(GAME.SYRINGUE.logo, GAME.SYRINGUE.rect)
GAME.SCREEN.screen.blit(GAME.PIPE.logo, GAME.PIPE.rect)
RUNNING = True

"""Game loop"""
while RUNNING:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
        elif GAME.PLAYER.health <= 0:
            RUNNING = False
            pygame.quit()
            print("You loose !" "End of the game.")
        elif GAME.GUARDIAN.health <= 0:
            RUNNING = False
            pygame.quit()
            print("You win !", "End of the game.")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and GAME.PLAYER.rect.y < GAME.SCREEN.outy:
                GAME.PLAYER.move_down()
                GAME.collect_items()
                GAME.guardian_collide()
            elif event.key == pygame.K_UP and GAME.PLAYER.rect.y > 0:
                GAME.PLAYER.move_up()
                GAME.collect_items()
                GAME.guardian_collide()
            elif event.key == pygame.K_LEFT and GAME.PLAYER.rect.x > 0:
                GAME.PLAYER.move_left()
                GAME.collect_items()
                GAME.guardian_collide()
            elif event.key == pygame.K_RIGHT and GAME.PLAYER.rect.x < GAME.SCREEN.outx:
                GAME.PLAYER.move_right()
                GAME.collect_items()
                GAME.guardian_collide()
            elif event.key == pygame.K_ESCAPE:
                RUNNING = False
                pygame.quit()
