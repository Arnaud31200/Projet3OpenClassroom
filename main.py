import pygame
from spritesgame import*
from Level import*

pygame.init()

class screen:
    def __init__(self, width, height):
        self.title = pygame.display.set_caption("Mac Gayver")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprite = self.width / 15
        self.outx = self.width - self.sprite
        self.outy = self.height - self.sprite

class game:
    def __init__(self):
        self.SCREEN = screen(300, 300)
        self.LEVEL = level(Level1, self.SCREEN.sprite, self.SCREEN)
        self.GUARDIAN = guardian(self.LEVEL)
        self.PLAYER = player(self.LEVEL, self.SCREEN.sprite, self.SCREEN, self.GUARDIAN)
        self.AIGUILLE = items(self.LEVEL, "ressource/aiguille.png", self.PLAYER)
        self.ETHER = items(self.LEVEL, "ressource/ether.png", self.PLAYER)
        self.SERINGUE = items(self.LEVEL, "ressource/seringue.png", self.PLAYER)
        self.TUBE = items(self.LEVEL, "ressource/tube_plastique.png", self.PLAYER)

    def collect_items(self):
        if self.PLAYER.rect == self.AIGUILLE.rect :
            self.PLAYER.life_attack_up()
        elif self.PLAYER.rect == self.ETHER.rect :
            self.PLAYER.life_attack_up()
        elif self.PLAYER.rect == self.SERINGUE.rect :
            self.PLAYER.life_attack_up()
        elif self.PLAYER.rect == self.TUBE.rect :
            self.PLAYER.life_attack_up()

    def collision_guardian(self):
        log_x, log_y = self.LEVEL.from_coord_to_grid(self.PLAYER.rect.x, self.PLAYER.rect.y)
        if self.LEVEL.LEVEL[log_y][log_x] == 4 :
            self.PLAYER.health = self.PLAYER.health - self.GUARDIAN.attack
            self.GUARDIAN.health = self.GUARDIAN.health - self.PLAYER.attack


GAME = game()
GAME.LEVEL.draw()
GAME.SCREEN.screen.blit(GAME.PLAYER.logo, GAME.PLAYER.rect)
GAME.SCREEN.screen.blit(GAME.GUARDIAN.logo, GAME.GUARDIAN.rect)
GAME.SCREEN.screen.blit(GAME.AIGUILLE.logo, GAME.AIGUILLE.rect)
GAME.SCREEN.screen.blit(GAME.ETHER.logo, GAME.ETHER.rect)
GAME.SCREEN.screen.blit(GAME.SERINGUE.logo, GAME.SERINGUE.rect)
GAME.SCREEN.screen.blit(GAME.TUBE.logo, GAME.TUBE.rect)

RUNNING = True

while RUNNING:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            RUNNING = False
            pygame.quit()
        elif GAME.PLAYER.health <= 0 :
            RUNNING = False
            pygame.quit()
            print("Vous avez perdu !")
        elif GAME.GUARDIAN.health <= 0 :
            RUNNING = False
            pygame.quit()
            print("Vous avez gagné !")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and GAME.PLAYER.rect.y < GAME.SCREEN.outy:
                GAME.PLAYER.move_down()
                GAME.collect_items()
                GAME.collision_guardian()
            elif event.key == pygame.K_UP and GAME.PLAYER.rect.y > 0 :
                GAME.PLAYER.move_up()
                GAME.collect_items()
                GAME.collision_guardian()
            elif event.key == pygame.K_LEFT and GAME.PLAYER.rect.x > 0 :
                GAME.PLAYER.move_left()
                GAME.collect_items()
                GAME.collision_guardian()
            elif event.key == pygame.K_RIGHT and GAME.PLAYER.rect.x < GAME.SCREEN.outx:
                GAME.PLAYER.move_right()
                GAME.collect_items()
                GAME.collision_guardian()
            elif event.key == pygame.K_ESCAPE:
                RUNNING = False
                pygame.quit()
           