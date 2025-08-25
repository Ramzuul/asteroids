import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def rotate(self, player_rotation):
        self.rotation = player_rotation