import pygame
from constants import *
from player import Player

def main():
    pygame.init() #Initialize Pygame
    clock = pygame.time.Clock() #Used to limit screen refresh rate to desired frame rate (fr)
    dt = 0
    fr = 60 #60 Hz framerate
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Set screen dimensions
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #Instantiate player object
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(fr) / 1000

if __name__ == "__main__":
    main()