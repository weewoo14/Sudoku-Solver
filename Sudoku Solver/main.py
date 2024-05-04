import pygame
from algorithm import *
from settings import *
from layout import *
from numpad import *
from solve_button import *
from copy import deepcopy

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku Solver!")
clock = pygame.time.Clock()

running = True
while running:
    mouse_xpos, mouse_ypos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, row in enumerate(grid_rect):
                for idx2, rect in enumerate(row):
                    if not is_collision(mouse_xpos,mouse_ypos,rect):
                        currently_select = []
                        currently_select.append(rect)
                        select_row,select_col = idx,idx2
            if currently_select:
                for row in (numpad_text):
                    for rect,text,color, in (row):
                        if not is_collision(mouse_xpos,mouse_ypos,rect):
                            if grid[select_row][select_col] != 0:
                                grid[select_row][select_col] = 0
                            else:
                                grid[select_row][select_col] = int(text)
             
            if not is_collision(mouse_xpos,mouse_ypos, solve_rect):
                if not solve:
                    for i in range(BOARD_HEIGHT):
                        for j in range(BOARD_WIDTH):
                            if grid[i][j] == 0:
                                grid[i][j] = '.'
                            else:
                                grid[i][j] = str(grid[i][j])
                    grid = sudoku_solve(grid)
                    if grid == False:
                        grid = deepcopy(restart_grid)
                    solve = True
                else:
                    grid = deepcopy(restart_grid)
                    solve = False
    screen.fill(BLACK)
    for idx,row in enumerate(grid_rect):
        for idx2,rect in enumerate(row):
            val = is_collision(mouse_xpos,mouse_ypos,rect)
            color = grid_color[val]
            pygame.draw.rect(screen, color, rect)
    for rect2 in currently_select:
        pygame.draw.rect(screen,grid_color[0],rect2)
    for row in numpad_layout:
        for rect in row:
            val = is_collision(mouse_xpos,mouse_ypos,rect)
            color = numpad_color[val]
            pygame.draw.rect(screen, color, rect)
    for row in numpad_text:
        for rect,text,color in row:
            GAME_FONT.render_to(screen,rect,text,color)
    for idx in range(BOARD_HEIGHT):
        for idx2 in range(BOARD_WIDTH):
            if grid[idx][idx2]:
                rect = grid_rect[idx][idx2]
                GAME_FONT.render_to(screen,rect,str(grid[idx][idx2]),BLUE)
    solve_val = not is_collision(mouse_xpos,mouse_ypos,solve_rect)
    pygame.draw.rect(screen, solve_color[solve_val], solve_rect)
    solve_font[solve].render_to(screen, solve_rect,solve_text[solve],WHITE)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()