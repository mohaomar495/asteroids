import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfields = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (asteroidfields, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(x, y)
    astfield = AsteroidField()    
    while True:
        log_state()
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    break

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
