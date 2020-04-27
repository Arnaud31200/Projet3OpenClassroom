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

    def from_coord_to_grid(self, posx, posy):
        i = max(0, int(posx / 20))
        j = max(0, int(posy / 20))
        return i, j

    def get_neighbour_blocks(self, level, i_start, j_start):
        blocks = list()
        for j in range(j_start, j_start+2):
            for i in range(i_start, i_start+2):
                if self.LEVEL[1] == i or j:
                    topleft = i*20, j*20
                    blocks.append(pygame.Rect((topleft), (20, 20)))
        return blocks
    
    def compute_penetration(self, block, old_rect, new_rect):
        dx_correction = dy_correction = 0.0
        if old_rect.bottom <= block.top < new_rect.bottom:
            dy_correction = block.top  - new_rect.bottom
        elif old_rect.top >= block.bottom > new_rect.top:
            dy_correction = block.bottom - new_rect.top
        if old_rect.right <= block.left < new_rect.right:
            dx_correction = block.left - new_rect.right
        elif old_rect.left >= block.right > new_rect.left:
            dx_correction = block.right - new_rect.left
        return dx_correction, dy_correction

    def bloque_sur_collision(self, level, old_posx, old_posy, new_posx, new_posy):
        old_rectxy = pygame.Rect((old_posx, old_posy), (20, 20))
        new_rectxy = pygame.Rect((new_posx, new_posy), (20, 20))
        i, j = self.from_coord_to_grid(new_posx, new_posy)
        collide_later = list()
        blocks = self.get_neighbour_blocks(self.LEVEL, i, j)
        for block in blocks:
            if not new_rectxy.colliderect(block):
                continue
 
        dx_correction, dy_correction = self.compute_penetration(block, old_rectxy, new_rectxy)
        new_rectxy.top += dy_correction
        new_rectxy.left += dx_correction

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