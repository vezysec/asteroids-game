import random
from circleshape import CircleShape
import pygame
from constants import ASTEROID_MAX_SPLIT_ANGLE, ASTEROID_MIN_RADIUS, ASTEROID_MIN_SPLIT_ANGLE, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(surface=screen, color="white", center=self.position,radius=self.radius,width=LINE_WIDTH)    
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_vector_a = self.velocity.rotate(random.uniform(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE))
            split_vector_b = self.velocity.rotate((-1) * random.uniform(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            roid_a = Asteroid(self.position.x, self.position.y, new_radius)
            roid_a.velocity = split_vector_a * 1.2
            roid_b = Asteroid(self.position.x, self.position.y, new_radius)
            roid_b.velocity = split_vector_b * 1.2


