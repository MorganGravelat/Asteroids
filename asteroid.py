import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_vel1 = pygame.math.Vector2.rotate(self.velocity, new_angle)
        new_vel2 = pygame.math.Vector2.rotate(-self.velocity, new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1, ast2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = new_vel1*1.2
        ast2.velocity = new_vel2*1.2


