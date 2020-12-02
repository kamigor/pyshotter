import pygame
from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W.....W....W',
    'W..WW....W.W',
    'W..........W',
    'W..........W',
    'W..W...WWW.W',
    'W...WW.....W',
    'WWWWWWWWWWWW'
]

world_map = set()
mini_map = set()
collisions_map = list()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collisions_map.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
