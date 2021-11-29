import pygame
from levels.Level1 import Level1

pygame.init()

screen = pygame.display.set_mode((1050, 700))
pygame.display.set_caption("Bugged In")

clock = pygame.time.Clock()

level = [Level1(screen, 2, 70, 70, 70, 35, 0.3, 5, 945, 595)]
level_index = 0

pygame.mixer.music.load("data/assets/music/bugsong.mp3")
pygame.mixer.music.play(-1)

playing = True

while playing:
    
    dt = clock.tick() / 1000

    level[level_index].run(dt)
    if level[level_index].level_changed == True:
        level_index += 1
    if level[level_index].game_quit:
        playing = False

    pygame.display.update()

pygame.quit()