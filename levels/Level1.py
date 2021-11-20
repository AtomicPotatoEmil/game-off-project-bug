import pygame

class Level1:

    def __init__(self, screen):
        self.screen = screen
        self.level_changed = False
        self.game_quit = False
        pass

    def run(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit = True
        pass