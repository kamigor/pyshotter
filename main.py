import pygame
from settings import *
from player import Player
from drawing import Drawing


pygame.init()
pygame.mouse.set_visible(False)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
pygame.display.set_caption("DOOM")
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)

pygame.mixer.music.load('sound/background_theme.mp3')
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(BLACK)
    drawing.background(player.angle)

    player.movement()

    drawing.radar(player)
    drawing.draw_map(player)

    drawing.fps(clock)
    pygame.display.flip()
    clock.tick()


