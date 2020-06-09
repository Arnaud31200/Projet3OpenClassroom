"""Import Modules"""
import pygame
from Level import Level
from Sprites import Player
from Sprites import Items
from Sprites import Guardian
from Game_structure import Screen
from Game_structure import Game

pygame.init()

"""game initialization"""
game = Game()
game.level.draw()
game.screen.screen.blit(game.player.logo, game.player.rect)
game.screen.screen.blit(game.guardian.logo, game.guardian.rect)
game.screen.screen.blit(game.needle.logo, game.needle.rect)
game.screen.screen.blit(game.ether.logo, game.ether.rect)
game.screen.screen.blit(game.syringue.logo, game.syringue.rect)
game.screen.screen.blit(game.pipe.logo, game.pipe.rect)

RUNNING = True

"""game loop"""
while RUNNING:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
        elif game.player.health <= 0:
            RUNNING = False
            pygame.quit()
            print("You loose !" "End of the game.")
        elif game.guardian.health <= 0:
            RUNNING = False
            pygame.quit()
            print("You win !", "End of the game.")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and game.player.rect.y < Screen.outy:
                game.player.move_down()
                game.collect_items()
                game.guardian_collide()
            elif event.key == pygame.K_UP and game.player.rect.y > 0:
                game.player.move_up()
                game.collect_items()
                game.guardian_collide()
            elif event.key == pygame.K_LEFT and game.player.rect.x > 0:
                game.player.move_left()
                game.collect_items()
                game.guardian_collide()
            elif event.key == pygame.K_RIGHT and game.player.rect.x < Screen.outx:
                game.player.move_right()
                game.collect_items()
                game.guardian_collide()
            elif event.key == pygame.K_ESCAPE:
                RUNNING = False
                pygame.quit()
