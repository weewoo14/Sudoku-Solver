from settings import *
from copy import deepcopy
grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]
restart_grid = deepcopy(grid)
grid_rect = []
currently_select = []
grid_color = {1: WHITE, 0:LIGHT_GRAY}
for row in range(BOARD_HEIGHT):
    row_rects = []
    for col in range(BOARD_HEIGHT):
        row_rects.append((100 * col + BOARD_OFFSET, 100 * row + BOARD_OFFSET, BOX_WIDTH,BOX_LENGTH))
    grid_rect.append(row_rects)
