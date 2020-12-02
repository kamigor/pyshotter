import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# player
PLAYER_POS = (HALF_WIDTH, HALF_HEIGHT)
PLAYER_ANGLE = 0
PLAYER_SPEED = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (40, 40, 40)
PURPLE = (110, 0, 110)
SKY_BLUE = (0, 186, 255)
YELLOW = (220, 220, 0)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_RATIO = 2 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
MODE_3D =True

