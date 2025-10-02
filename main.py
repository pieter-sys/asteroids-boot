# from tkinter.constants import S
import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    whitestar = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        whitestar.update(dt)

        # draw
        screen.fill((0, 0, 0))

        whitestar.draw(screen)

        # present
        pygame.display.flip()

        # set 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
