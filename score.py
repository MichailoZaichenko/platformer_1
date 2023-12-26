import pygame
from coin import SCORE

# Initialize the pygame library
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Create a font object
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    # ...

    # Draw the score
    score_text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()