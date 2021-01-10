# from pygame.math import Vector2 as vec


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
DIAMETROx = int(MAZE_WIDTH/19) - 2
DIAMETRO = int(MAZE_HEIGHT/21) -2

RADIOS = DIAMETROx/2
START_POINT =[MAZE_WIDTH/2 -    DIAMETROx/2 ,TOP_BOT_BUFF/2 + 15.5 * MAZE_HEIGHT/21 - DIAMETRO/2]

vel_x = RADIOS/2 - 0.75 * MAZE_WIDTH/19/2/3                #tenho que ajustar a velocidade
vel_y = RADIOS/2 - 0.75 * MAZE_WIDTH/19/2/3 #RADIOS/2 - 0.75 * MAZE_HEIGHT/21/3/2


MAZE_LIMITS = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],    #0 == points, 1 == walls , 2 == big points, 3 = nothing
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
    [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,3,1,3,1,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,3,3,3,3,3,3,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1],
    [3,3,3,3,0,3,3,1,1,1,1,1,3,3,0,3,3,3,3],
    [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,3,3,3,3,3,3,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
    [1,2,0,1,0,0,0,0,0,3,0,0,0,0,0,1,0,2,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

BLOCKS_POS = [[-1, 8], [-1, 10], [21,8], [21,10], [-2, 8], [-2, 10], [22,8], [22,10]]
for y in range(len(MAZE_LIMITS)):
    for x in range(len(MAZE_LIMITS[y])):
        if MAZE_LIMITS[y][x] == 1:
            BLOCKS_POS.append([x,y])
            
# mob settings