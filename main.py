import pygame
from game import*

pygame.init()

GAME = game()
RUNNING = True

while RUNNING:
    num_ligne = 0
    for ligne in GAME.LEVEL.LEVEL:
        num_case = 0
        for number in ligne:
            a = num_case * GAME.SCREEN.sprite
            b = num_ligne * GAME.SCREEN.sprite
            if number == 1:
                GAME.SCREEN.screen.blit(GAME.LEVEL.Wall, (a,b))
            elif number == 0 or number == 5 or number == 6 or number == 7 or number == 8:
                GAME.SCREEN.screen.blit(GAME.LEVEL.Floor, (a,b))
            elif number == 3 or number == 4:
                GAME.SCREEN.screen.blit(GAME.LEVEL.Start, (a,b))
            num_case += 1
        num_ligne += 1
    
    GAME.SCREEN.screen.blit(GAME.PLAYER.logo, GAME.PLAYER.rect)
    GAME.SCREEN.screen.blit(GAME.GUARDIAN.logo, GAME.GUARDIAN.rect)

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
           