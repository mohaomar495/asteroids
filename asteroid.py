import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(
                surface,
                "white",
                self.position,
                self.radius,
                LINE_WIDTH
                )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        randomAngle = random.uniform(20, 50)
        new_vectorL = self.velocity.rotate(randomAngle)
        new_vectorS = self.velocity.rotate(-randomAngle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        as1 = Asteroid(self.position.x, self.position.y, new_radius)
        as2 = Asteroid(self.position.x, self.position.y, new_radius)

        as1.velocity = new_vectorL * 1.2
        as2.velocity = new_vectorS * 1.2
