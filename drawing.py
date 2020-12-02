import pygame
from settings import *
from map import world_map, mini_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self, angle):
        pygame.draw.rect(self.sc, SKY_BLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def radar(self, player):
        self.ray_casting(player.pos, player.angle)

    def draw_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y),
                         (map_x + 12 * math.cos(player.angle), map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, GREEN, (x, y, MAP_TILE, MAP_TILE))

        self.sc.blit(self.sc_map, MAP_POS)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, RED)
        self.sc.blit(render, FPS_POS)

    def ray_casting(self, player_pos, player_angle):

        def mapping(x, y):
            return (x // TILE) * TILE, (y // TILE) * TILE

        depth_v, depth_h = 0, 0
        xh, yv = 0, 0
        ox, oy = player_pos
        xm, ym = mapping(ox, oy)
        cur_angle = player_angle - HALF_FOV

        for ray in range(NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)

            # intersection with vertical lines
            x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
            for i in range(0, WIDTH, TILE):
                depth_v = (x - ox) / cos_a
                yv = oy + depth_v * sin_a
                if mapping(x + dx, yv) in world_map:
                    break
                x += dx * TILE

            # intersection with horizontal lines
            y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
            for i in range(0, HEIGHT, TILE):
                depth_h = (y - oy) / sin_a
                xh = ox + depth_h * cos_a
                if mapping(xh, y + dy) in world_map:
                    break
                y += dy * TILE

            depth = depth_v if depth_v < depth_h else depth_h

            # Fish eye correction
            depth *= math.cos(player_angle - cur_angle)
            # W/A for proj_heiht = PROJ_COEFF / depth <- division by 0 error
            depth = max(depth, 0.00001)
            proj_height = min(int(PROJ_RATIO / depth), 2 * HEIGHT)

            main_color = 255 / (1 + depth * depth * 0.00002)
            color = (main_color, main_color // 2, main_color // 3)
            pygame.draw.rect(self.sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            cur_angle += DELTA_ANGLE

    def ray_casting_basic(self, player_pos, player_angle):
        """
        Non-optimized algorithm
        :param player_pos:
        :param player_angle:
        :return:
        """
        cur_angle = player_angle - HALF_FOV
        xo, yo = player_pos
        # print('xo=' + str(xo), 'yo=' + str(yo))
        for ray in range(NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            for depth in range(MAX_DEPTH):
                x = xo + depth * cos_a
                y = yo + depth * sin_a
                if (x // TILE * TILE, y // TILE * TILE) in world_map:
                    if MODE_3D:
                        depth *= math.cos(player_angle - cur_angle)
                        proj_heiht = PROJ_RATIO / depth
                        c = 255 / (1 + depth * depth * 0.00002)
                        color = (c, c // 2, c // 3)
                        pygame.draw.rect(self.sc, color, (ray * SCALE, HALF_HEIGHT - proj_heiht // 2, SCALE, proj_heiht))
                    else:
                        pygame.draw.line(self.sc, DARK_GRAY, player_pos, (x, y), 1)
                    break

            cur_angle += DELTA_ANGLE

