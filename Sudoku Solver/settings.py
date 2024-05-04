import pygame
import pygame.freetype
pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
GAME_FONT = pygame.freetype.Font("ComicSansMS3.ttf", 95)
RESTART_FONT = pygame.freetype.Font("ComicSansMS3.ttf",65)
TEXT_OFFSET = 10

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
DARK_GREEN = (0,158,0)
GRAY = (100,100,100)
LIGHT_GRAY = (160,160,160)
RED = (255,0,0)
ORANGE = (255,103,0)
BLUE = (0,0,255)
LIGHT_BLUE = (13,232,253)

BOARD_WIDTH = 9
BOARD_HEIGHT = 9
BOARD_OFFSET = 50

BOX_WIDTH = 95
BOX_LENGTH = 95

NUMPAD_WIDTH = 3
NUMPAD_LENGTH = 3
NUMPAD_OFFSET = 1100
TOTAL_NUMPAD = 9

def is_collision(x,y,rect):
    x1,y1,x2,y2 = rect[0],rect[1],rect[0]+rect[2],rect[1]+rect[3]
    return x < x1 or x > x2 or y < y1 or y > y2
