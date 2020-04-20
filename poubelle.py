def from_coord_to_grid(pos):
        x, y = pos
        i = max(0, int(x / 20))
        j = max(0, int(y / 20))
        return i, j
    
def get_neighbour_blocks(niveau, i_start, j_start):
    blocks = list()
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if niveau[j][i] == 1:
                topleft = i*20, j*20
                blocks.append(pygame.Rect((topleft), (20, 20)))
    return blocks

def collision(niveau, pos):
    rect = pygame.Rect(pos, (20, 20))
    i, j = from_coord_to_grid(pos)
    for block in get_neighbour_blocks(niveau, i, j):
        if rect.colliderect(block):
            return True
    return False
