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

# Simple DDA line drawing function
def draw_dda_line(x1, y1, x2, y2, color):
    """Draw a line using DDA algorithm"""
    dx = x2 - x1
    dy = y2 - y1
    
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        screen.set_at((int(x1), int(y1)), color)
        return
    
    x_inc = dx / steps
    y_inc = dy / steps
    
    x, y = x1, y1
    
    for _ in range(int(steps) + 1):
        screen.set_at((int(x), int(y)), color)
        x += x_inc
        y += y_inc

class SimpleBicycle:
    def __init__(self, x, y):
        self.x = x  # Center position of bicycle
        self.y = y
        self.speed = 3
        self.wheel_radius = 30
        self.wheel_rotation = 0
    
    def draw(self):
        """Draw the entire bicycle"""
        # Calculate wheel positions
        back_wheel_x = self.x - 60
        back_wheel_y = self.y
        front_wheel_x = self.x + 60
        front_wheel_y = self.y
        
        # Draw wheels using Midpoint Circle Algorithm
        midpoint_circle(back_wheel_x, back_wheel_y, self.wheel_radius, GRAY)
        midpoint_circle(front_wheel_x, front_wheel_y, self.wheel_radius, GRAY)
        
        # Draw frame using DDA lines
        seat_x = self.x - 20
        seat_y = self.y - 50
        handle_x = self.x + 40
        handle_y = self.y - 30
        
        # Main triangle frame
        draw_dda_line(back_wheel_x, back_wheel_y, seat_x, seat_y, BLUE)
        draw_dda_line(seat_x, seat_y, front_wheel_x, front_wheel_y, BLUE)
        draw_dda_line(back_wheel_x, back_wheel_y, front_wheel_x, front_wheel_y, BLUE)
        
        # Seat
        draw_dda_line(back_wheel_x, back_wheel_y, seat_x, seat_y, RED)
        
        # Handlebar
        draw_dda_line(front_wheel_x, front_wheel_y, handle_x, handle_y, RED)
        draw_dda_line(handle_x - 15, handle_y, handle_x + 15, handle_y, RED)
    
    def move(self):
        """Move the bicycle and rotate wheels"""
        self.x += self.speed
        
        # Rotate wheels (visual effect)
        self.wheel_rotation += 0.2
        
        # Reset position when off screen
        if self.x > WIDTH + 100:
            self.x = -100

