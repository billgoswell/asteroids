from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_roid = Asteroid(self.position.x, self.position.y, new_radius) 
            new_roid.velocity = self.velocity.rotate(random_angle)*1.2
            new_roid2 = Asteroid(self.position.x, self.position.y, new_radius) 
            new_roid2.velocity = self.velocity.rotate(-random_angle)*1.2
            
