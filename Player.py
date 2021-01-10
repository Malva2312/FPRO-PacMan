import pygame
import math
from pygame.math import Vector2 as vec
from settings import *
    
class Player:
    def __init__(self, app, point):
        self.app = app
        self.start_point = point
        self.center = [point[0] + RADIOS, point[1] + RADIOS -  TOP_BOT_BUFF]
        
        self.animation_count = 0 
        
        self.load()
        
    def update(self):
        pass
    
    def draw(self):
        
        
        if self.app.move_left:
            if self.animation_count == 0 or self.animation_count == 1 or self.animation_count == 4 or self.animation_count == 5:
                self.pac_man = self.pac_man02 
            
            if self.animation_count== 2 or self.animation_count == 3 :
                self.pac_man = self.pac_man1
                
            if self.animation_count== 6 or self.animation_count == 7:
                self.pac_man = self.pac_man3
            
            self.pac_man = pygame.transform.flip(self.pac_man, True, False)
        
        
        
        elif self.app.move_right: 
            if self.animation_count == 0 or self.animation_count == 1 or self.animation_count == 4 or self.animation_count == 5:
                self.pac_man = self.pac_man02 
            
            if self.animation_count== 2 or self.animation_count == 3 :
                self.pac_man = self.pac_man1
                
            if self.animation_count== 6 or self.animation_count == 7:
                self.pac_man = self.pac_man3
                
                
        elif self.app.move_up:
            if self.animation_count == 0 or self.animation_count == 1 or self.animation_count == 4 or self.animation_count == 5:
                self.pac_man = self.pac_man_mid_up 
            
            if self.animation_count== 2 or self.animation_count == 3 :
                self.pac_man = self.pac_man_open_up
                
            if self.animation_count== 6 or self.animation_count == 7:
                self.pac_man = self.pac_man3
                 
        elif self.app.move_down:
            if self.animation_count == 0 or self.animation_count == 1 or self.animation_count == 4 or self.animation_count == 5:
                self.pac_man = self.pac_man_mid_up 
            
            if self.animation_count== 2 or self.animation_count == 3 :
                self.pac_man = self.pac_man_open_up
                
            if self.animation_count== 6 or self.animation_count == 7:
                self.pac_man = self.pac_man3
            
            self.pac_man = pygame.transform.flip(self.pac_man, False, True)
        
        else:
            self.pac_man = self.pac_man02 
            
            
        self.app.screen.blit(self.pac_man, (self.start_point))
        
        
        
    def load(self):
        # self.pac_man = pygame.image.load("pac_man_fill.png")
        # 125 * 150 PX
        
        self.pac_man02 = pygame.image.load("pacman_mid2.png") #estado 0 (meio aberto) estado 2 
        self.pac_man1 = pygame.image.load("pacman_open2.png") #estado 1 (aberto)
        self.pac_man3 = pygame.image.load("pac_man_fill2.png")   #estado 3
        
        self.pac_man_mid_up = pygame.image.load("pacman_mid_up2.png")
        self.pac_man_open_up = pygame.image.load("pacman_open_up2.png")
        
        
        self.pac_man02 = pygame.transform.scale(self.pac_man02, (DIAMETROx,DIAMETRO))
        self.pac_man1 = pygame.transform.scale(self.pac_man1, (DIAMETROx,DIAMETRO))
        self.pac_man3 = pygame.transform.scale(self.pac_man3, (DIAMETROx,DIAMETRO))
        
        self.pac_man_mid_up = pygame.transform.scale(self.pac_man_mid_up, (DIAMETROx,DIAMETRO))
        self.pac_man_open_up = pygame.transform.scale(self.pac_man_open_up, (DIAMETROx,DIAMETRO))
        
        
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