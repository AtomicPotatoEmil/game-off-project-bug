import pygame

class Player:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.player_img = pygame.image.load("data/assets/sprites/player/player.png").convert_alpha()
        self.can_go_right = True
        self.can_go_left = True
        self.can_go_up = True
        self.can_go_down = True
        self.rect = self.player_img.get_rect(x = self.x, y = self.y)
    
    def update(self):
        self.screen.blit(self.player_img, (self.x, self.y))
        self.rect = self.player_img.get_rect(x = self.x, y = self.y)