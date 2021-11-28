import pygame

class Player:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.player_img_up = pygame.image.load("data/assets/sprites/player/player.png").convert_alpha()
        self.player_img_right = pygame.transform.rotate(self.player_img_up, -90)
        self.player_img_down = pygame.transform.rotate(self.player_img_up, 180)
        self.player_img_left = pygame.transform.rotate(self.player_img_up, 90)
        self.direction_value = 1
        self.current_direction = self.player_img_up

        self.can_go_right = True
        self.can_go_left = True
        self.can_go_up = True
        self.can_go_down = True

        self.rect = self.current_direction.get_rect(x = self.x, y = self.y)
    
    def update(self):
        if self.direction_value == 1:
            self.current_direction = self.player_img_up
        elif self.direction_value == 2:
            self.current_direction = self.player_img_right
        elif self.direction_value == 3:
            self.current_direction = self.player_img_down
        elif self.direction_value == 4:
            self.current_direction = self.player_img_left
        self.screen.blit(self.current_direction, (self.x, self.y))
        self.rect = self.current_direction.get_rect(x = self.x, y = self.y)