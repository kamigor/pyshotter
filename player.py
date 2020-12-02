import pygame
from settings import *
from map import collisions_map


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
        future_position = self.player_rect.copy()
        future_position.move_ip(dx, dy)
        collision_indexes = future_position.collidelistall(collisions_map)

        if len(collision_indexes):
            delta_x, delta_y = 0, 0
            for collision_index in collision_indexes:
                collision_rect = collisions_map[collision_index]
                if dx > 0:
                    delta_x += future_position.right - collision_rect.left
                else:
                    delta_x += collision_rect.right - future_position.left
                if dy > 0:
                    delta_y += future_position.bottom - collision_rect.top
                else:
                    delta_y += collision_rect.bottom - future_position.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_x < delta_y:
                dx = 0

        self.x += dx
        self.y += dy

    def movement(self):
        self.key_control()
        self.mouse_control()
        self.player_rect.center = self.x, self.y

    def key_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            exit()
        if keys[pygame.K_w]:
            dx = PLAYER_SPEED * cos_a
            dy = PLAYER_SPEED * sin_a
            self.detect_collisions(dx, dy)
        if keys[pygame.K_s]:
            dx = -PLAYER_SPEED * cos_a
            dy = -PLAYER_SPEED * sin_a
            self.detect_collisions(dx, dy)
        if keys[pygame.K_a]:
            dx = PLAYER_SPEED * sin_a
            dy = -PLAYER_SPEED * cos_a
            self.detect_collisions(dx, dy)
        if keys[pygame.K_d]:
            dx = -PLAYER_SPEED * sin_a
            dy = PLAYER_SPEED * cos_a
            self.detect_collisions(dx, dy)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05

    def mouse_control(self):
        if pygame.mouse.get_focused():
            diff = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += diff * self.sensitivity

