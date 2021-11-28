import pygame
from levels.Level1 import Level1

screen = pygame.display.set_mode((1050, 700))
pygame.display.set_caption("Bugged In")

clock = pygame.time.Clock()

level = [Level1(screen, 3)]
level_index = 0

playing = True

while playing:
    
    dt = clock.tick() / 1000

    level[level_index].run(dt)
    if level[level_index].game_quit:
        playing = False

    pygame.display.update()

pygame.quit()