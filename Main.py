"""Import Modules"""
import pygame
from Level import Level
from Sprites import Player
from Sprites import Items
from Sprites import Guardian
from Game_structure import Screen
from Game_structure import Game

pygame.init()

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
