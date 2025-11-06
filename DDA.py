import pygame
import math

def draw_line_dda(surface, x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    
    if abs(dy) > abs(dx):
        steps = abs(dy)
    else:
        steps = abs(dx)
    
    if steps == 0:
        return
    
    x_inc = dx / steps
    y_inc = dy / steps
    
    x, y = x1, y1
    
    for i in range(steps + 1):
        surface.set_at((round(x), round(y)), color)
        x += x_inc
        y += y_inc

# Usage
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

draw_line_dda(screen, 200, 200, 1000, 600, (255, 0, 0))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()