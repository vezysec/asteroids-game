import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state

def main():
    ### Game initialization
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    ### Game Loop
    while True:
        ## log game state for debugging
        log_state()
        ## check Player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ## update Game world

        ## Draw Game State
        
        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
