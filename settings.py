from pygame.math import Vector2 as vec


# screen settings
TOP_BOT_BUFF = 50
WIDTH, HEIGHT = 224*2, 288*2 +TOP_BOT_BUFF
MAZE_WIDTH, MAZE_HEIGHT = WIDTH, HEIGHT - TOP_BOT_BUFF
FPS = 60

# colour settings
BLACK = (0, 0, 0) #BLACK RGB
RED = (202, 52, 51)
GRAY = (107, 107, 107)
WHITE =(255, 255, 255)
YELLOW =(255, 255, 0)

#source settings
TEXT_SIZE = 16
START_SOURCE = "arial black"

# playes settings
RADIOS = MAZE_HEIGHT/21/2 - 3
START_POINT =[MAZE_WIDTH/2, MAZE_HEIGHT/2 + MAZE_HEIGHT/21]
vel = 3
# mob settings