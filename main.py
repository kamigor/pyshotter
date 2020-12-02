import pygame
from settings import *
from player import Player
from drawing import Drawing


pygame.init()
pygame.mouse.set_visible(False)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DOOM")
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(BLACK)
    player.movement()

    drawing.draw_map(player)
    drawing.radar(player)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick()


