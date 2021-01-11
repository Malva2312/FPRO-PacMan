import pygame
import math
from settings import *
import random


class Mob:
    def __init__(self, app, point):  #, Color
        self.app = app
        self.blinky_start_point = point
        self.center = [point[0] + RADIOS, point[1] + RADIOS -  TOP_BOT_BUFF]
        
        
        self.blinky_move_up = False
        self.blinky_move_down = False
        self.blinky_move_left = False
        self.blinky_move_right = False
        
        
        self.count = 0
        
        self.load()
        
    
    
    def load(self):
        
        self.blinky = pygame.image.load("blinky.png")
        self.blinky = pygame.transform.flip(self.blinky, True, False)
        
        self.blinky = pygame.transform.scale(self.blinky, (MOB_DIAMETROx, MOB_DIAMETRO))
        self.blinky_0 = self.blinky
    
    def matrix_pos(self,position):
        
        if [(self.blinky_start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.blinky_start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.blinky_start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.blinky_start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS :
            
            self.move_right = False
        else:
            self.move_right = True
        
        if [(self.blinky_start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.blinky_start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.blinky_start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.blinky_start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS :
            
            self.move_left = False
        else:
            self.move_left = True
        
        if [self.blinky_start_point[0]//(MAZE_WIDTH/19), (self.blinky_start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.blinky_start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.blinky_start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in MOB_BLOCKS:
            
            self.move_down = False
        else:
            self.move_down = True
            
        if [self.blinky_start_point[0]//(MAZE_WIDTH/19), (self.blinky_start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.blinky_start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.blinky_start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in MOB_BLOCKS:
            
            self.move_up = False
        else:
            self.move_up = True
            

  
    
  
    
  
    
    def move(self, vel_x, vel_y):
        self.matrix_pos(self.blinky_start_point)        
        
        
        X, Y = abs(self.app.player.start_point[0] - self.blinky_start_point[0]),  abs(self.app.player.start_point[1] - self.blinky_start_point[1])
        
        
        ABSx = abs( self.app.player.start_point[0] - self.blinky_start_point[0]) > 1
        ABSy = abs(  self.app.player.start_point[1] - self.blinky_start_point[1] ) > 1
        
        if self.count == 0:
            if X >= Y:
                if (self.app.player.start_point[0] < self.blinky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = True
                    self.blinky_move_right = False
                    
                elif self.app.player.start_point[0] > self.blinky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = True
                    
                elif self.app.player.start_point[1] < self.blinky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.blinky_move_up = True
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = False
                    
                    
                elif self.app.player.start_point[1] > self.blinky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.blinky_move_up = False
                    self.blinky_move_down = True
                    self.blinky_move_left = False
                    self.blinky_move_right = False
                
                
            
                else:
                    self.count = 1
                    
            elif Y >= X:
                if self.app.player.start_point[1] < self.blinky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.blinky_move_up = True
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = False
                    
                    
                elif self.app.player.start_point[1] > self.blinky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.blinky_move_up = False
                    self.blinky_move_down = True
                    self.blinky_move_left = False
                    self.blinky_move_right = False
                
                elif (self.app.player.start_point[0] < self.blinky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = True
                    self.blinky_move_right = False
                    
                elif self.app.player.start_point[0] > self.blinky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = True
                
                else:
                    self.count = 1
                    
                    
        else:
            
            if self.count % 8 == 0:
                
                    a = random.randint(0,3)
                    
                    if a == 0:
                        self.blinky_move_up = False
                        self.blinky_move_down = False
                        self.blinky_move_left = True
                        self.blinky_move_right = False
                    elif a == 1:
                        self.blinky_move_up = True
                        self.blinky_move_down = False
                        self.blinky_move_left = False
                        self.blinky_move_right = False
                    elif a == 2:
                        self.blinky_move_up = False
                        self.blinky_move_down = True
                        self.blinky_move_left = False
                        self.blinky_move_right = False
                    elif a == 3:
                        self.blinky_move_up = False
                        self.blinky_move_down = False
                        self.blinky_move_left = False
                        self.blinky_move_right = True
                    
                    
            self.count += 1
            if self.count == 16 * 16:
                self.count = 0
        
            
        
        
        
        
        
        
        # elif not( (self.app.player.start_point[0] < self.blinky_start_point[0] and self.move_left) or (self.app.player.start_point[0] > self.blinky_start_point[0] and self.move_right) or (self.app.player.start_point[1] < self.blinky_start_point[1] and self.move_up) or (self.app.player.start_point[1] > self.blinky_start_point[1] and self.move_down)  ):
        #     None
            
            
        
        if self.blinky_start_point[0]  - MAZE_WIDTH/19 + 1< 0:
                self.blinky_move_up = False
                self.blinky_move_down = False
                self.blinky_move_right = False
                self.blinky_move_left = True
        
        if self.blinky_start_point[0] +  MOB_DIAMETROx + MAZE_WIDTH/19 -1 > MAZE_WIDTH:
                self.blinky_move_up = False
                self.blinky_move_down = False
                self.blinky_move_right = False
                self.blinky_move_left = True
        
        # 330.9342105263149
        # 96.0657894736841
        
        
        
        if self.blinky_move_left and self.move_left:
            
            if self.blinky_start_point[0] - vel_x + DIAMETROx < 0:
                self.blinky_start_point[0] = MAZE_WIDTH - (self.blinky_start_point[0] + vel_x)
                
            else:
                self.blinky_start_point[0] -= vel_x
                    
                
        elif self.move_right and self.blinky_move_right:
            
            if self.blinky_start_point[0] + vel_x  > MAZE_WIDTH:
                self.blinky_start_point[0] = MAZE_WIDTH - (self.blinky_start_point[0]  + DIAMETRO)
                
            else:
                self.blinky_start_point[0] += vel_x
            
            
        elif self.move_up and self.blinky_move_up:
            
            self.blinky_start_point[1] -= vel_y
            
            
        elif self.move_down and self.blinky_move_down:
            self.blinky_start_point[1] += vel_y
            
            
        # print((self.blinky__left and self.move_left) or (self.move_right and self.blinky__right) or (self.move_up and self.blinky__up) or (self.move_down and self.blinky__down))
        # print(self.blinky_move_up ,self.blinky_move_down, self.blinky_move_left, self.blinky_move_right)
        # print("up", self.blinky_move_up, self.move_up)
        # print("down", self.blinky_move_down, self.move_down)
        # print("left", self.blinky_move_left, self.move_left)
        # print("right", self.blinky_move_right, self.move_right)
        
        
        
    def draw(self):
        if self.blinky_move_left:
            self.blinky = self.blinky_0
        
        elif self.blinky_move_right:
            self.blinky = pygame.transform.flip(self.blinky_0, True, False)
            
        else:
            self.blinky = self.blinky
        
        self.app.screen.blit(self.blinky, (self.blinky_start_point))
            
        
