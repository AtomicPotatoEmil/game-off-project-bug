import pygame
from Tile import FloorTile, WallTile
from Player import Player

class Level1:

    def __init__(self, screen, color_id):
        self.screen = screen
        self.color_id = color_id
        self.level_changed = False
        self.game_quit = False

        self.level_template = (
            (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            (2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2),
            (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
        )

        self.floor_tiles = []
        self.wall_tiles = []

        for y in range(len(self.level_template)):
            for x in range(len(self.level_template[y])):
                if self.level_template[y][x] == 1:
                    self.floor_tiles.append(FloorTile(self.screen, self.color_id, x * 35, y * 35))
                if self.level_template[y][x] == 2:
                    self.wall_tiles.append(WallTile(self.screen, self.color_id, x * 35, y * 35))
        
        self.player_instance = [Player(self.screen, 70, 70, 3)]

    def run(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit = True
            if event.type == pygame.KEYDOWN:
                for player in self.player_instance:
                    if player.can_go_right:
                        if event.key == pygame.K_RIGHT:
                            player.x += 35
                            player.direction_value = 2
                            player.can_go_left = True
                            player.can_go_down = True
                            player.can_go_up = True
                    if player.can_go_left:
                        if event.key == pygame.K_LEFT:
                            player.x -= 35
                            player.direction_value = 4
                            player.can_go_right = True
                            player.can_go_down = True
                            player.can_go_up = True
                    if player.can_go_up:
                        if event.key == pygame.K_UP:
                            player.y -= 35
                            player.direction_value = 1
                            player.can_go_left = True
                            player.can_go_down = True
                            player.can_go_right = True
                    if player.can_go_down:
                        if event.key == pygame.K_DOWN:
                            player.y += 35
                            player.direction_value = 3
                            player.can_go_left = True
                            player.can_go_right = True
                            player.can_go_up = True
        
        self.screen.fill((0, 0, 0))
        
        for tile in self.floor_tiles:
            for player in self.player_instance:
                if tile.rect.colliderect(player.rect):
                    tile.has_collided = True
            tile.draw()
        
        for player in self.player_instance:
            player.update()
        
        for tile in self.wall_tiles:
            for player in self.player_instance:
                if player.right_ray.colliderect(tile.rect):
                    player.can_go_right = False
                    print("hit")
                if player.left_ray.colliderect(tile.rect):
                    player.can_go_left = False
                    print("hit")
                if player.upper_ray.colliderect(tile.rect):
                    player.can_go_up = False
                    print("hit")
                if player.bottom_ray.colliderect(tile.rect):
                    player.can_go_down = False
                    print("hit")
            tile.draw()    
        