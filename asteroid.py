import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_velocity_one = self.velocity.rotate(angle)
            new_velocity_two = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_one.velocity = new_velocity_one
            new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_two.velocity = new_velocity_two
            return new_asteroid_one, new_asteroid_two
