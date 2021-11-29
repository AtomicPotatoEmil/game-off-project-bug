import pygame
from TileParticle import Particle

class FloorTile:

    def __init__(self, screen, tile_id, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        if tile_id == 1:
            self.floor = pygame.image.load("data/assets/sprites/floor/red_floor.png").convert_alpha()
        elif tile_id == 2:
            self.floor = pygame.image.load("data/assets/sprites/floor/green_floor.png").convert_alpha()
        elif tile_id == 3:
            self.floor = pygame.image.load("data/assets/sprites/floor/blue_floor.png").convert_alpha()

        self.purple_tile = pygame.image.load("data/assets/sprites/floor/purple_floor.png").convert_alpha()
        self.corruption_particles = Particle(self.screen, self.x, self.y, self.purple_tile)
        self.has_collided = False
        self.cleansed = False
        self.rect = self.floor.get_rect(x = self.x, y = self.y)
    
    def draw(self):
        if self.has_collided and not self.cleansed:
            self.screen.blit(self.purple_tile, (self.x, self.y))
            self.corruption_particles.emit_particles()
        else:
            self.screen.blit(self.floor, (self.x, self.y))



class WallTile:

    def __init__(self, screen, tile_id, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        if tile_id == 1:
            self.wall = pygame.image.load("data/assets/sprites/wall/red_wall.png").convert_alpha()
        elif tile_id == 2:
            self.wall = pygame.image.load("data/assets/sprites/wall/green_wall.png").convert_alpha()
        elif tile_id == 3:
            self.wall = pygame.image.load("data/assets/sprites/wall/blue_wall.png").convert_alpha()

        self.rect = self.wall.get_rect(x = self.x, y = self.y)
    
    def draw(self):
        self.screen.blit(self.wall, (self.x, self.y))
    

class HazardTile:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img = pygame.image.load("data/assets/sprites/floor/hazard.png").convert_alpha()
        self.rect = self.img.get_rect(x = self.x, y = self.y)
        self.hazard_particles = Particle(self.screen, self.x, self.y, self.img)
    
    def draw(self):
        self.hazard_particles.emit_particles()

class EnemySpawnTile:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img = pygame.image.load("data/assets/sprites/floor/enemy_spawn.png").convert_alpha()
    
    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))


class ExitTile:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img = pygame.image.load("data/assets/sprites/floor/exit.png").convert_alpha()
        self.particles = Particle(self.screen, self.x, self.y, self.img)
        self.particles2 = Particle(self.screen, self.x + 35, self.y, self.img)
        self.particles3 = Particle(self.screen, self.x, self.y  + 35, self.img)
        self.particles4 = Particle(self.screen, self.x + 35, self.y  + 35, self.img)
        self.rect = pygame.Rect(self.x, self.y, 70, 70)
    
    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
        self.screen.blit(self.img, (self.x + 35, self.y))
        self.screen.blit(self.img, (self.x, self.y + 35))
        self.screen.blit(self.img, (self.x + 35, self.y + 35))
        self.particles.emit_particles()
        self.particles2.emit_particles()
        self.particles3.emit_particles()
        self.particles4.emit_particles()
    