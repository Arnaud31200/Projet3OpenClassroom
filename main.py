import pygame
pygame.init()

class game:
    def __init__(self):
        self.PLAYER = player()
        self.GUARDIAN = guardian()
        self.LEVEL = level()
        self.PRESSED = {}
    
class level:
    def __init__(self):
        self.labyrinth = [
        [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]]
        self.Floor = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(0,160,20,20)
        self.Wall = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(40,0,20,20)
        self.Start = pygame.image.load("ressource/floor-tiles-20x20.png").subsurface(160,20,20,20)

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.attack = 0
        self.velocity = 5
        self.logo = pygame.transform.scale(pygame.image.load("ressource/MacGyver.png"),(20, 20))  
        self.rect = self.logo.get_rect()      
        self.rect.x = 0
        self.rect.y = 0
    
    def move_right(self):
            self.rect.x += self.velocity
    
    def move_left(self):
            self.rect.x -= self.velocity

    def move_up(self):
            self.rect.y -= self.velocity

    def move_down(self):
            self.rect.y += self.velocity

class guardian(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.attack = 0
        self.logo = pygame.transform.scale(pygame.image.load("ressource/Gardien.png"),(20, 20))
        self.rect = self.logo.get_rect()
        self.rect.x = 280
        self.rect.y = 280

pygame.display.set_caption("Mac Gayver")
SCREEN = pygame.display.set_mode((300, 300))
GAME = game()
RUNNING = True

while RUNNING:
    num_ligne = 0
    for ligne in GAME.LEVEL.labyrinth:
        num_case = 0
        for number in ligne:
            a = num_case * 20
            b = num_ligne * 20
            if number == 1:
                SCREEN.blit(GAME.LEVEL.Wall, (a,b))
            elif number == 0:
                SCREEN.blit(GAME.LEVEL.Floor, (a,b))
            elif number == 3:
                SCREEN.blit(GAME.LEVEL.Start, (a,b))
            num_case += 1
        num_ligne += 1
    SCREEN.blit(GAME.PLAYER.logo, GAME.PLAYER.rect)
    SCREEN.blit(GAME.GUARDIAN.logo, GAME.GUARDIAN.rect)
    
    if GAME.PRESSED.get(pygame.K_RIGHT) and GAME.PLAYER.rect.x < 280:
        GAME.PLAYER.move_right()
    elif GAME.PRESSED.get(pygame.K_LEFT) and GAME.PLAYER.rect.x > 0:
        GAME.PLAYER.move_left()
    elif GAME.PRESSED.get(pygame.K_UP)and GAME.PLAYER.rect.y > 0:
        GAME.PLAYER.move_up()
    elif GAME.PRESSED.get(pygame.K_DOWN)and GAME.PLAYER.rect.y < 280:
        GAME.PLAYER.move_down()
    
    pygame.display.flip()    
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            GAME.PRESSED[event.key] = True
        elif event.type == pygame.KEYUP:
            GAME.PRESSED[event.key] = False