import pygame

class Tile:

    def __init__(self, screen, tile_id, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        if tile_id == 1:
            self.floor = pygame.image.load("data/assets/sprites/floor/red_floor.png")
        elif tile_id == 2:
            self.floor = pygame.image.load("data/assets/sprites/floor/green_floor.png")
        elif tile_id == 3:
            self.floor = pygame.image.load("data/assets/sprites/floor/blue_floor.png")

        self.purple_tile = pygame.image.load("data/assets/sprites/floor/purple_floor.png")
        self.has_collided = False

        self.tile_rect = self.floor.get_rect(x = self.x, y = self.y)
    
    def draw(self):
        if self.has_collided:
            self.screen.blit(self.purple_tile, (self.x, self.y))
        else:
            self.screen.blit(self.floor, (self.x, self.y))