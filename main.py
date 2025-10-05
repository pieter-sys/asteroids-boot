import pygame
import constants
import sys
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    CircleShape.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    whitestar = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    field = AsteroidField()

    dt = clock.tick(60) / 1000

    while True:
        # handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        updatable.update(dt)

        # collision detection
        for asteroid in asteroids:
            if asteroid.collision(whitestar):
                print("Game Over!")
                sys.exit()

        # draw
        screen.fill((0, 0, 0))

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        # present
        pygame.display.flip()

        # set 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
