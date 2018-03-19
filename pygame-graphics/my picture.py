# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

#Colors
RED = (255, 0, 0)
ORANGE = (255, 125 , 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PRETTY_BLUE = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (225, 0, 225)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #draw time
    screen.fill(PRETTY_BLUE)
    pygame.draw.rect(screen, BLUE, [0, 400, 800, 200])
    pygame.draw.arc(screen, YELLOW, [200, 200, 400, 400], 0, math.pi, 200)
    pygame.draw.circle(screen, WHITE, [100, 100], 50)
    pygame.draw.circle(screen, WHITE, [140, 150], 50)
    pygame.draw.circle(screen, WHITE, [170, 100], 50)
    pygame.draw.circle(screen, WHITE, [200, 150], 50)
    pygame.draw.circle(screen, WHITE, [230, 100], 50)
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)
    
# Close window and quit
pygame.quit()

            
