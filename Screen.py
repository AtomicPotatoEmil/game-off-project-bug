import pygame
from pygame.constants import QUIT

class StartScreen:

    def __init__(self, screen):
        self.screen = screen
        self.game_quit = False
        self.level_changed = False
        self.img = pygame.image.load("data/assets/screens/start.png")
        

    def run(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.level_changed = True
        self.screen.blit(self.img, (0, 0))

class WinScreen:

    def __init__(self, screen):
        self.screen = screen
        self.game_quit = False
        self.level_changed = False
        self.img = pygame.image.load("data/assets/screens/win.png")
        pass

    def run(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit = True
        self.screen.blit(self.img, (0, 0))