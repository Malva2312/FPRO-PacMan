from pygame.math import Vector2 as vec


# screen settings
TOP_BOT_BUFF = 50
WIDTH, HEIGHT = 224*2, 288*2 +TOP_BOT_BUFF
MAZE_WIDTH, MAZE_HEIGHT = WIDTH, HEIGHT - TOP_BOT_BUFF
FPS = 60

#colour settings
BLACK = (0, 0, 0) #BLACK RGB
RED = (202, 52, 51)
GRAY = (107, 107, 107)
WHITE =(255, 255, 255)
YELLOW =(255, 255, 0)
ORANJE = (240, 134, 37)

#source settings
TEXT_SIZE = 16
START_SOURCE = "arial black"

# playes settings
DIAMETRO = int(MAZE_WIDTH/19-5)
RADIOS = DIAMETRO//2
START_POINT =[MAZE_WIDTH/2 -RADIOS +1 ,MAZE_HEIGHT/2 +2*MAZE_HEIGHT/21+ -RADIOS]
vel_x = MAZE_WIDTH/19
vel_y = MAZE_HEIGHT/21


MAZE_LIMITS = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],    #A matriz tem erros, amanhã corrijo
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
    [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,1,1,1,0,1,0,0,0,2,0,0,0,1,0,1,1,1,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

BLOCKS_POS = []
for y in range(len(MAZE_LIMITS)):
    for x in range(len(MAZE_LIMITS[y])):
        if MAZE_LIMITS[y][x] == 1:
            BLOCKS_POS.append([x,y])
            
# mob settings