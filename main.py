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
        self.PLAYER = player(self.LEVEL, self.SCREEN.sprite)
        self.GUARDIAN = guardian(self.LEVEL)
        self.AIGUILLE = items(self.LEVEL, "ressource/aiguille.png")
        self.ETHER = items(self.LEVEL, "ressource/ether.png")
        self.SERINGUE = items(self.LEVEL, "ressource/seringue.png")
        self.TUBE = items(self.LEVEL, "ressource/tube_plastique.png")

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
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and GAME.PLAYER.rect.y < GAME.SCREEN.outy:
                GAME.PLAYER.move_down()
            elif event.key == pygame.K_UP and GAME.PLAYER.rect.y > 0 :
                GAME.PLAYER.move_up()
            elif event.key == pygame.K_LEFT and GAME.PLAYER.rect.x > 0 :
                GAME.PLAYER.move_left()
            elif event.key == pygame.K_RIGHT and GAME.PLAYER.rect.x < GAME.SCREEN.outx:
                GAME.PLAYER.move_right()
            elif event.key == pygame.K_ESCAPE:
                RUNNING = False
                pygame.quit()
           