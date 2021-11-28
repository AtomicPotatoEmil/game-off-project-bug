import random

class Particle():
    def __init__(self, screen, x,y, tile):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.range = range(1)
    
        self.screen = screen
        self.tile = tile

        self.list = []

    def emit_particles(self):
        for particle in self.range:
            vel_x = ((random.randint(0, 20) / 10 -1) / 10)
            vel_y = ((random.randint(0, 20) / 10 -1) / 10)
            self.list.append(self.screen.blit(self.tile, (self.x, self.y)))
            self.x -= vel_x
            self.y -= vel_y
            
            if self.x < self.start_x - 2 or self.x > self.start_x + 2:
                self.x = self.start_x

            if self.y < self.start_y - 2 or self.y > self.start_y + 2:
                self.y = self.start_y