import pygame
import math
from pygame.math import Vector2 as vec
from settings import *

    
class Player:
    def __init__(self, app, point):
        self.app = app
        self.start_point = point
        self.center = [point[0] + RADIOS, point[1] + RADIOS -  TOP_BOT_BUFF]
        
        self.load()
        
    def update(self):
        pass
    
    def draw(self):
        self.app.screen.blit(self.pac_man, (self.start_point))
    
        
    def load(self):
        # self.pac_man = pygame.image.load("pac_man_fill.png")
        self.pac_man = pygame.image.load("pac_man_fill2.png")   # 125 * 150 PX
        self.pac_man = pygame.transform.scale(self.pac_man, (DIAMETROx,DIAMETRO))
        
    def matrix_pos(self,position):
        
        if [(self.start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in BLOCKS_POS or [(self.start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in BLOCKS_POS :
            
            self.move_right = False
        else:
            self.move_right = True
        
        if [(self.start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in BLOCKS_POS or [(self.start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in BLOCKS_POS :
            
            self.move_left = False
        else:
            self.move_left = True
        
        if [self.start_point[0]//(MAZE_WIDTH/19), (self.start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in BLOCKS_POS or [(self.start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in BLOCKS_POS:
            
            self.move_down = False
        else:
            self.move_down = True
            
        if [self.start_point[0]//(MAZE_WIDTH/19), (self.start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in BLOCKS_POS or [(self.start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in BLOCKS_POS:
            
            self.move_up = False
        else:
            self.move_up = True