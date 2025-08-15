import pygame
import random

from circleshape import *   

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255, 255), (int(self.position.x), int(self.position.y)), (int(self.radius)), 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle1 = random.uniform (20, 50)
            angle2 = angle1 * -1
            velocity1 = self.velocity.rotate(angle1)
            velocity2 = self.velocity.rotate(angle2)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2

            
            
        