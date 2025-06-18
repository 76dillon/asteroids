import sys
import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init() #Initialize Pygame
    clock = pygame.time.Clock() #Used to limit screen refresh rate to desired frame rate (fr)
    dt = 0
    fr = 60 #60 Hz framerate
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Set screen dimensions
    #Create two groups. First are objects that can be updated, second is all objects that can be drawn
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Set both groups as containers for the player
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #Instantiate player object
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game over!")
                sys.exit()
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(fr) / 1000

if __name__ == "__main__":
    main()