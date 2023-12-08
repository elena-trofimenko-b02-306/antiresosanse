
from phys_modelling import *


def drawer(screen,gruz_driven,gruz_free,spring1,spring2):
    pygame.draw.rect(screen, (0,150,150), (0, 400, 800, 200))
    pygame.draw.rect(screen, (0, 150, 150), (0, 0, 150, 600))
    pygame.draw.aaline(screen, (100,100,100), [150, 350], [gruz_driven.x, 350])
    pygame.draw.rect(screen, (0, 250, 0), (gruz_driven.x, 300, 100, 100))
    pygame.draw.aaline(screen, (100, 100, 100), [gruz_driven.x+100, 350],[gruz_free.x, 350] )
    pygame.draw.rect(screen, (0, 250, 0), (gruz_free.x, 300, 100, 100))