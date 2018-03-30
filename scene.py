# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 30, 0)
WHITE = (255, 255, 255)
DBLUE = (0, 0, 255)
YELLOW = (255, 255, 175)
LBLUE = (0, 225, 204)
GRAY = (166, 166, 166)
DGREEN = (0, 51, 0)
BROWN = (102, 51, 0)
BLACK = (0, 0, 0)

# Make trees
num_trees = 3
trees = []
for i in range(num_trees):
    x = random.randrange(0, 800)
    y = 300
    loc = [x, y]
    trees.append(loc)

def draw_tree(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.rect(screen, BROWN, [x + 20, y + 70, 20, 40], 0)
    pygame.draw.ellipse(screen, DGREEN, [x, y, 60, 80], 0)
   

#game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.K_SPACE:
            pass

        
    '''sky'''
    screen.fill(BLACK)
    
    '''ground'''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200], 0)
    
    '''trees'''
    for t in trees:
        draw_tree(t)

    '''moon'''
    




                        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
