import pygame

class Enemy:

    def __init__(self, screen, x, y, move_time):
        self.screen = screen
        self.x = x
        self.y = y
        self.enemy_img = pygame.image.load("data/assets/sprites/enemy/enemy.png").convert_alpha()
        self.rect = self.enemy_img.get_rect(x = self.x, y = self.y)
        self.move_time = move_time
        self.time = move_time
        self.is_moving = False
        
    def update(self, dt):
        if self.is_moving == False:
            self.move_time -= 1 * dt
        if self.move_time <= 0:
            self.is_moving = True
            self.move_time = self.time
        self.screen.blit(self.enemy_img, (self.x, self.y))
        self.rect = self.enemy_img.get_rect(x = self.x, y = self.y)