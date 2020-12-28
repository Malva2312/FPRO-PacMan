import pygame
import math
from pygame.math import Vector2 as vec
from settings import *

class Player:
    def __init__(self, app, point):
        self.app = app
        self.start_point = point
        
        # self.grid_point = point
        # self.pix_point = vec(self.grid_point.x * self.app.cell_width, self.grid_point.x*self.app.cell_height + TOP_BOT_BUFF)
        # print(self.pix_point)
        
        
    def update(self):
        pass
    
    def draw(self):
        pygame.draw.circle(self.app.background, YELLOW, self.start_point, RADIOS)
        