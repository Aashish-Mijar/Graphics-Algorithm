import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bicycle with Midpoint Circle Wheels")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
GRAY = (150, 150, 150)

# Midpoint Circle Algorithm (same as Bresenham's circle)
def midpoint_circle(cx, cy, radius, color):
    """Draw a circle using Midpoint Circle Algorithm"""
    x = 0
    y = radius
    d = 1 - radius  # Initial decision parameter
    
    # Draw points in all 8 octants
    while x <= y:
        # Plot points in all octants
        screen.set_at((cx + x, cy + y), color)
        screen.set_at((cx - x, cy + y), color)
        screen.set_at((cx + x, cy - y), color)
        screen.set_at((cx - x, cy - y), color)
        screen.set_at((cx + y, cy + x), color)
        screen.set_at((cx - y, cy + x), color)
        screen.set_at((cx + y, cy - x), color)
        screen.set_at((cx - y, cy - x), color)
        
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

