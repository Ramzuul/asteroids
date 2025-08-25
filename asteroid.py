from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.0, 50.0)
        random_angle_1, random_angle_2 = self.velocity.rotate(random_angle), self.velocity.rotate(random_angle * -1)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1, new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius), Asteroid(self.position[0], self.position[1], new_radius)

        new_asteroid_1.velocity = random_angle_1 * 1.2
        new_asteroid_2.velocity = random_angle_2 * 1.2