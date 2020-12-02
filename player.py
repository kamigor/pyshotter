import pygame
import math

from settings import *
# from map import map_collisions


class Player:
    def __init__(self):
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.sensitivity = 0.002
        # collisions
        self.side = 50
        self.player_rect = pygame.Rect(self.x, self.y, self.side, self.side)

    @property
    def pos(self):
        return self.x, self.y

    def detect_collisions(self, dx, dy):
        pass

    def movement(self):
        self.key_control()
        self.mouse_control()

    def key_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            exit()
        if keys[pygame.K_w]:
            self.x += PLAYER_SPEED * cos_a
            self.y += PLAYER_SPEED * sin_a
        if keys[pygame.K_s]:
            self.x += -PLAYER_SPEED * cos_a
            self.y += -PLAYER_SPEED * sin_a
        if keys[pygame.K_a]:
            self.x += PLAYER_SPEED * sin_a
            self.y += -PLAYER_SPEED * cos_a
        if keys[pygame.K_d]:
            self.x += -PLAYER_SPEED * sin_a
            self.y += PLAYER_SPEED * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05

    def mouse_control(self):
        if pygame.mouse.get_focused():
            diff = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += diff * self.sensitivity


