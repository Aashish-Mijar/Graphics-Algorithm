import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple DDA Object Moving in Line")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)

# Simple DDA line drawing function
def draw_dda_line(x1, y1, x2, y2, color):
    """Draw a line using DDA algorithm"""
    dx = x2 - x1
    dy = y2 - y1
    
    # Determine number of steps
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        pygame.draw.circle(screen, color, (int(x1), int(y1)), 1)
        return
    
    # Calculate increments
    x_inc = dx / steps
    y_inc = dy / steps
    
    # Start from first point
    x, y = x1, y1
    
    # Draw points at each step
    for _ in range(int(steps) + 1):
        pygame.draw.circle(screen, color, (int(x), int(y)), 2)
        x += x_inc
        y += y_inc

# Create a simple square object
class SimpleSquare:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = RED
        self.speed = 2
        self.direction = 1  # 1 for right, -1 for left
    
    def get_corners(self):
        """Return the four corners of the square"""
        half = self.size // 2
        return [
            (self.x - half, self.y - half),  # top-left
            (self.x + half, self.y - half),  # top-right
            (self.x + half, self.y + half),  # bottom-right
            (self.x - half, self.y + half)   # bottom-left
        ]
    
    def draw(self):
        """Draw square using DDA lines"""
        corners = self.get_corners()
        
        # Draw four sides using DDA
        for i in range(4):
            x1, y1 = corners[i]
            x2, y2 = corners[(i + 1) % 4]
            draw_dda_line(x1, y1, x2, y2, self.color)
    
    def move(self):
        """Move the square in a straight line"""
        self.x += self.speed * self.direction
        
        # Bounce when hitting screen edges
        half = self.size // 2
        if self.x + half >= WIDTH:
            self.direction = -1
            self.color = BLUE
        elif self.x - half <= 0:
            self.direction = 1
            self.color = RED

# Create the square object
square = SimpleSquare(100, 300, 100)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                # Reset square position
                square.x = 100
                square.y = 300
    
    # Clear screen
    screen.fill(BLACK)
    
   
    
    # Update and draw the square
    square.move()
    square.draw()
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
