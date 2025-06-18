import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vel_vec1 = self.velocity.rotate(random_angle)
        vel_vec2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #Create two new smaller faster asteroids
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = vel_vec1*1.2
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = vel_vec2*1.2
    
    def add_pts(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            num_pts = NUM_PTS_SMALL
        elif self.radius == ASTEROID_MIN_RADIUS*2:
            num_pts = NUM_PTS_MED
        else:
            num_pts = NUM_PTS_BIG
        return num_pts



        