import pygame
from grid import Grid
from blocks import * 

pygame.init()
pygame.display.set_caption('Pygame Tetris')

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BG_COLOR = (102,161,255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock() 
run = True

game_grid = Grid()
game_grid.print_grid()

block = LBlock()      

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Drawing
    screen.fill(BG_COLOR)
    game_grid.draw(screen)

    block.draw(screen)
    pygame.display.update()
    clock.tick(60) 


pygame.quit()