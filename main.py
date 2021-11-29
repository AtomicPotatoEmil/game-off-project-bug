import pygame
from Level import Level
import LevelMatrices as lm

pygame.init()

screen = pygame.display.set_mode((1050, 700))
pygame.display.set_caption("Bugged In")

clock = pygame.time.Clock()


level = [
    Level(screen, lm.level1, 1, 70, 70, 3, 70, 35, 0.3, 5, 945, 595),
    Level(screen, lm.level2, 2, 945, 595, 1, 945, 630, 0.3, 5, 35, 35),
    Level(screen, lm.level3, 3, 70, 70, 3, 70, 35, 0.3, 5, 630, 140),
    Level(screen, lm.level4, 1, 665, 140, 3, 665, 105, 0.3, 5, 455, 315),
    Level(screen, lm.level5, 2, 455, 315, 1, 455, 350, 0.3, 5, 35, 35),
    Level(screen, lm.level6, 3, 70, 70, 3, 70, 35, 0.3, 5, 910, 560),
    Level(screen, lm.level7, 1, 945, 560, 1, 945, 595, 0.3, 5, 805, 560),
    Level(screen, lm.level8, 2, 945, 595, 4, 980, 595, 0.2, 5, 35, 595),
    Level(screen, lm.level9, 3, 70, 595, 1, 70, 630, 0.3, 5, 490, 35),
    Level(screen, lm.level10, 1, 490, 70, 3, 490, 35, 0.3, 5, 490, 595)
    ]
level_index = 0

pygame.mixer.music.load("data/assets/music/bugsong.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

playing = True

while playing:
    
    dt = clock.tick() / 1000

    level[level_index].run(dt)
    if level[level_index].level_changed:
        level_index += 1
    if level[level_index].game_quit:
        playing = False

    pygame.display.update()

pygame.quit()