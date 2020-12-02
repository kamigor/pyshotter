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
# map_collisions = list()

for j, row in enumerate(text_map):
    # print('j: ' + str(j), 'row: ' + row)
    for i, char in enumerate(row):
        # print('i: ' + str(i), 'char: ' + char)
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            # map_collisions.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
    # print (world_map)
