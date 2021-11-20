import pygame

screen = pygame.display.set_mode((1050, 700))
pygame.display.set_caption("Bugged In")

clock = pygame.time.Clock()

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    dt = clock.tick() / 1000

    pygame.display.update()

pygame.quit()