import pygame
from pygame.constants import K_w
from Tile import FloorTile, WallTile, HazardTile, EnemySpawnTile, ExitTile
from Player import Player
from Enemy import Enemy

class Level:

    def __init__(self, screen, level_matrix, color_id, player_x, player_y, player_direction, enemy_x, enemy_y, enemy_speed, enemy_spawn_time, exit_x, exit_y):
        self.screen = screen
        self.color_id = color_id
        self.player_start_x = player_x
        self.player_start_y = player_y
        self.enemy_speed = enemy_speed
        self.level_changed = False
        self.game_quit = False

        self.level_template = level_matrix

        self.floor_tiles = []
        self.wall_tiles = []
        self.hazard_tiles = []

        for y in range(len(self.level_template)):
            for x in range(len(self.level_template[y])):
                if self.level_template[y][x] == 1:
                    self.floor_tiles.append(FloorTile(self.screen, self.color_id, x * 35, y * 35))
                if self.level_template[y][x] == 2:
                    self.wall_tiles.append(WallTile(self.screen, self.color_id, x * 35, y * 35))
        
        self.player_instance = [Player(self.screen, player_x, player_y, player_direction)]
        self.enemy_instance = []

        self.enemy_spawn_timer = enemy_spawn_time
        self.spawn_time = 1
        self.enemy_path = []
        self.enemy_spawn_tile = EnemySpawnTile(self.screen, enemy_x, enemy_y)

        self.exit_tile = ExitTile(self.screen, exit_x, exit_y)


    def run(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit = True
            if event.type == pygame.KEYDOWN:
                for player in self.player_instance:
                    if player.can_go_right:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            player.x += 35
                            player.direction_value = 2
                            player.can_go_left = True
                            player.can_go_down = True
                            player.can_go_up = True
                    if player.can_go_left:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            player.x -= 35
                            player.direction_value = 4
                            player.can_go_right = True
                            player.can_go_down = True
                            player.can_go_up = True
                    if player.can_go_up:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            player.y -= 35
                            player.direction_value = 1
                            player.can_go_left = True
                            player.can_go_down = True
                            player.can_go_right = True
                    if player.can_go_down:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            player.y += 35
                            player.direction_value = 3
                            player.can_go_left = True
                            player.can_go_right = True
                            player.can_go_up = True
        
        if len(self.enemy_instance) == 0:
            self.enemy_spawn_timer -= 1 * dt
        
        if self.enemy_spawn_timer <= 0:
            self.enemy_instance.append(Enemy(self.screen, self.enemy_spawn_tile.x, self.enemy_spawn_tile.y, self.enemy_speed))
            self.enemy_spawn_timer = self.spawn_time
        
        self.screen.fill((0, 0, 0))
        
        for tile in self.floor_tiles:
            for player in self.player_instance:
                if tile.rect.colliderect(player.rect):
                    if tile.has_collided == False:
                        self.enemy_path.append(tile.x)
                        self.enemy_path.append(tile.y)
                        print(self.enemy_path)
                    tile.has_collided = True
            for enemy in self.enemy_instance:
                if tile.rect.colliderect(enemy.rect):
                    tile.cleansed = True
            tile.draw()
        
        self.enemy_spawn_tile.draw()
        self.exit_tile.draw()
        
        for tile in self.hazard_tiles:
            for player in self.player_instance:
                if tile.rect.colliderect(player.rect):
                    self.reset_level(self.player_start_x, self.player_start_y)
            tile.draw()
        
        
        for enemy in self.enemy_instance:
            if len(self.enemy_path) > 0:
                if enemy.is_moving:
                    self.hazard_tiles.append(HazardTile(self.screen, self.enemy_path[0], self.enemy_path[1]))
                    enemy.x = self.enemy_path.pop(0)
                    enemy.y = self.enemy_path.pop(0)
                    enemy.is_moving = False
            for player in self.player_instance:
                if player.rect.colliderect(enemy.rect):
                    self.reset_level(self.player_start_x, self.player_start_y)
            enemy.update(dt)
        
        for player in self.player_instance:
            player.update()
            if player.rect.colliderect(self.exit_tile.rect):
                self.level_changed = True
                print("hit")
        
        for tile in self.wall_tiles:
            for player in self.player_instance:
                if player.right_ray.colliderect(tile.rect):
                    player.can_go_right = False
                if player.left_ray.colliderect(tile.rect):
                    player.can_go_left = False
                if player.upper_ray.colliderect(tile.rect):
                    player.can_go_up = False
                if player.bottom_ray.colliderect(tile.rect):
                    player.can_go_down = False
            tile.draw()
        
    def reset_level(self, start_x, start_y):
        for player in self.player_instance:
            player.x = start_x
            player.y = start_y
            player.can_go_right = True
            player.can_go_left = True
            player.can_go_down = True
            player.can_go_up = True

        self.hazard_tiles.clear()
        self.enemy_path.clear()
        self.enemy_instance.clear()
        for tile in self.floor_tiles:
            tile.has_collided = False
            tile.cleansed = False
        
        