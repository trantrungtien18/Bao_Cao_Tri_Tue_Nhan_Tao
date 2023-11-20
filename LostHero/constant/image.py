import pygame

import spritesheet
from constant.dimension import *
from pygame_functions import *

# Init Pygame:
WIN = screenSize(WIDTH + 200, WIDTH)

pygame.init()
pygame.display.set_caption("Path Finding Algorithm")
pygame.init()

duckImg = pygame.transform.scale(pygame.image.load("./image/Duck.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
finishLineImg = pygame.transform.scale(pygame.image.load("./image/FinishLine.png"), (WIDTH // ROWS
                                                                                     , WIDTH // ROWS))
grassImg = pygame.transform.scale(pygame.image.load("./image/Grass.png"), (WIDTH // ROWS
                                                                           , WIDTH // ROWS))
waterImg = pygame.transform.scale(pygame.image.load("./image/Water.png"), (WIDTH // ROWS
                                                                           , WIDTH // ROWS))
landImg = pygame.transform.scale(pygame.image.load("./image/Land.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
flagImg = pygame.transform.scale(pygame.image.load("./image/Flag.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
stopImg = pygame.transform.scale(pygame.image.load("./image/Stop.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
startImg = pygame.transform.scale(pygame.image.load("./image/start.jpg"), (WIDTH // ROWS
                                                                           , WIDTH // ROWS))
footPrintImg = pygame.transform.scale(pygame.image.load("./image/Footprint.png"), (WIDTH // ROWS
                                                                                   , WIDTH // ROWS))

player_idle_image = pygame.transform.scale(pygame.image.load("./image/player/idle.png"), (WIDTH * 2 // ROWS,
                                                                                          WIDTH * 2 // ROWS))

player_back_sheet = pygame.image.load("./image/player/Back/spritesheet.png").convert_alpha()
player_front_sheet = pygame.image.load("./image/player/Front/spritesheet.png").convert_alpha()
player_left_sheet = pygame.image.load("./image/player/Left_Side/spritesheet.png").convert_alpha()
player_right_sheet = pygame.image.load("./image/player/Right_Side/spritesheet.png").convert_alpha()


player_back = spritesheet.SpriteSheet(player_back_sheet)
player_front = spritesheet.SpriteSheet(player_front_sheet)
player_left = spritesheet.SpriteSheet(player_left_sheet)
player_right = spritesheet.SpriteSheet(player_right_sheet)
PLAYER_WIDTH = 16500 // 15
PLAYER_HEIGHT = 1100
PLAYER_SPEED = 10


def get_player_image(sheet, frame):
    return sheet.get_image(frame,PLAYER_WIDTH,PLAYER_HEIGHT,0.1)
