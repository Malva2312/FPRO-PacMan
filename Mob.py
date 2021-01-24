import pygame
import math
from settings import *
import random
                                  

class Mob:
    def __init__(self, app, point, png):  #, Color
        self.app = app
        self.mob_start_point = point
        self.center = [point[0] + RADIOS, point[1] + RADIOS -  TOP_BOT_BUFF]
        
        self.png = png
        
        self.mob_move_up = False
        self.mob_move_down = False
        self.mob_move_left = False
        self.mob_move_right = False
        
        self.mirror_move = None
        
        self.app = app
        
        self.clock = pygame.time.Clock() 
        
        self.count = 0
        
        self.load()
        
        
        self.power_up_mob = False
    
    
    def load(self):
        
        self.mob = pygame.image.load(self.png)
        self.mob = pygame.transform.flip(self.mob, True, False)
        
        self.mob = pygame.transform.scale(self.mob, (MOB_DIAMETROx, MOB_DIAMETRO))
        self.mob_0 = self.mob
        
        self.scared = pygame.image.load("png/scared ghost.png")
        self.scared = pygame.transform.scale(self.scared, (MOB_DIAMETROx, MOB_DIAMETRO))
    
    def matrix_pos(self,position):
        
        
        if self.mob_start_point[1] + MOB_DIAMETRO  < 8 * MAZE_HEIGHT/21 + TOP_BOT_BUFF:
            MOB_BLOCKS = BLOCKS_POS
        else:
            MOB_BLOCKS = BLOCKS
        
        
        if [(self.mob_start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.mob_start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.mob_start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.mob_start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS :
            
            self.move_right = False
        else:
            self.move_right = True
        
        if [(self.mob_start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.mob_start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.mob_start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.mob_start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS :
            
            self.move_left = False
        else:
            self.move_left = True
        
        if [self.mob_start_point[0]//(MAZE_WIDTH/19), (self.mob_start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.mob_start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.mob_start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in MOB_BLOCKS:
            
            self.move_down = False
        else:
            self.move_down = True
            
        if [self.mob_start_point[0]//(MAZE_WIDTH/19), (self.mob_start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.mob_start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.mob_start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in MOB_BLOCKS:
            
            self.move_up = False
        else:
            self.move_up = True
            

    
    def mob_colision(self):
        
        if self.app.state == "playing" and self.power_up_mob == False and ( ((self.mob_start_point[0] + MOB_DIAMETROx/2 - self.app.player.start_point[0] - DIAMETROx/2 )**2 + (self.mob_start_point[1] + MOB_DIAMETRO/2 - self.app.player.start_point[1] - DIAMETRO/2)**2) <= (DIAMETROx*(4/5))**2):
            
            self.app.lifes -= 1
            self.power_up_mob = False
            if self.app.lifes ==0:
                self.app.state = "game over"
                
            else:
                self.app.state = "pregame"
                pygame.time.delay(1200)
                
                
                
        elif self.app.state == "playing"  and self.power_up_mob  and ( ((self.mob_start_point[0] + MOB_DIAMETROx/2 - self.app.player.start_point[0] - DIAMETROx/2 )**2 + (self.mob_start_point[1] + MOB_DIAMETRO/2 - self.app.player.start_point[1] - DIAMETRO/2)**2) <= (DIAMETROx*(4/5))**2):
            
            self.app.bonus += 1
            self.mob_start_point = INKY_START_POINT.copy()
            self.app.score += 200 * self.app.bonus
            self.power_up_mob = False
            pygame.time.delay(450)
    
    
    def move(self, vel_x, vel_y, goal):
        self.matrix_pos(self.mob_start_point)        
        
        
        X, Y = abs(goal[0] - self.mob_start_point[0]),  abs(goal[1] - self.mob_start_point[1])
        
        ABSx = abs( goal[0] - self.mob_start_point[0]) > 1
        ABSy = abs(  goal[1] - self.mob_start_point[1] ) > 1
        

        
############################################################################## BASIC MOVEMENT INSTROCTIONS
        
        if self.count == 0:
            if X >= Y:
                if (goal[0] < self.mob_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = True
                    self.mob_move_right = False
                    
                elif goal[0] > self.mob_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = True
                    
                elif goal[1] < self.mob_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.mob_move_up = True
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = False
                    
                    
                elif goal[1] > self.mob_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.mob_move_up = False
                    self.mob_move_down = True
                    self.mob_move_left = False
                    self.mob_move_right = False
                
                
            
                else:
                    self.count = 1
                    
            elif Y >= X:
                if goal[1] < self.mob_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.mob_move_up = True
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = False
                    
                    
                elif goal[1] > self.mob_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.mob_move_up = False
                    self.mob_move_down = True
                    self.mob_move_left = False
                    self.mob_move_right = False
                
                elif (goal[0] < self.mob_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = True
                    self.mob_move_right = False
                    
                elif goal[0] > self.mob_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = True
                
                else:
                    self.count = 1
                    
                    

############################################################################## RANDOM LOGIC                    

        else:
            ############ if stuck: random logic##############
            # path = list(filter())
            moves = [[self.move_down, "DOWN"], [self.move_up, "UP"], [self.move_right, "RIGHT"], [self.move_left, "LEFT"]]
            
            MOVEMENT = list(filter(lambda x: x[0], moves))
            
            if [True, self.mirror_move] in MOVEMENT and len(MOVEMENT)>1:
                MOVEMENT.remove([True, self.mirror_move])
            # print(MOVEMENT)    
            MOVEMENT = random.choice([x for x in MOVEMENT])
            
            
            if MOVEMENT[1] == "UP":
                self.mob_move_up = True
                self.mob_move_down = False
                self.mob_move_left = False
                self.mob_move_right = False
                
            elif MOVEMENT[1] == "DOWN":
                self.mob_move_up = False
                self.mob_move_down = True
                self.mob_move_left = False
                self.mob_move_right = False
            
            elif MOVEMENT[1] == "RIGHT":
                self.mob_move_up = False
                self.mob_move_down = False
                self.mob_move_left = False
                self.mob_move_right = True
        
            elif MOVEMENT[1] == "LEFT":
                self.mob_move_up = False
                self.mob_move_down = False
                self.mob_move_left = True
                self.mob_move_right = False
        '''
            # random.shuffle(PATH)
            pos = [0, 0]
            pos[0] = (self.mob_start_point[0] - goal[0]) + self.mob_start_point[0]
            pos[1] = (self.mob_start_point[1] - goal[1]) + self.mob_start_point[1]
            
            
            X, Y = abs(pos[0] - self.mob_start_point[0]),  abs(pos[1] - self.mob_start_point[1])
        
            ABSx = abs( pos[0] - self.mob_start_point[0]) > 1
            ABSy = abs(  pos[1] - self.mob_start_point[1] ) > 1
            
            
            if X >= Y:
                if (pos[0] < self.mob_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = True
                    self.mob_move_right = False
                    
                elif pos[0] > self.mob_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = True
                    
                elif pos[1] < self.mob_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.mob_move_up = True
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = False
                    
                    
                elif pos[1] > self.mob_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.mob_move_up = False
                    self.mob_move_down = True
                    self.mob_move_left = False
                    self.mob_move_right = False
            
                
            
                    
            elif Y >= X:
                if pos[1] < self.mob_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.mob_move_up = True
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = False
                    
                    
                elif pos[1] > self.mob_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.mob_move_up = False
                    self.mob_move_down = True
                    self.mob_move_left = False
                    self.mob_move_right = False
                
                elif (pos[0] < self.mob_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = True
                    self.mob_move_right = False
                    
                elif pos[0] > self.mob_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.mob_move_up = False
                    self.mob_move_down = False
                    self.mob_move_left = False
                    self.mob_move_right = True
            '''
        self.count += 1
        if self.count == 16 * 8:
                self.count = 0
                
            
################################################################################     
        
################################################################################    
    
############################################################################## OUT OF MAZE LMITS
        
        if self.mob_start_point[0]  - MAZE_WIDTH/19 + 1< 0:
                self.mob_move_up = False
                self.mob_move_down = False
                self.mob_move_right = False
                self.mob_move_left = True
        
        if self.mob_start_point[0] +  MOB_DIAMETROx + MAZE_WIDTH/19 -1 > MAZE_WIDTH:
                self.mob_move_up = False
                self.mob_move_down = False
                self.mob_move_right = False
                self.mob_move_left = True
        
        # 330.9342105263149
        # 96.0657894736841
        
        
   ###################### MOVEMENT CALCULATION ##############################     
        if self.mob_move_left and self.move_left:
            self.mirror_move = "RIGHT"
            
            if self.mob_start_point[0] - vel_x + DIAMETROx < 0:
                self.mob_start_point[0] = MAZE_WIDTH - (self.mob_start_point[0] + vel_x)
                
            else:
                self.mob_start_point[0] -= vel_x
                    
                
        elif self.move_right and self.mob_move_right:
            self.mirror_move = "LEFT"
            if self.mob_start_point[0] + vel_x  > MAZE_WIDTH:
                self.mob_start_point[0] = MAZE_WIDTH - (self.mob_start_point[0]  + DIAMETRO)
                
            else:
                self.mob_start_point[0] += vel_x
            
            
        elif self.move_up and self.mob_move_up:
            self.mirror_move = "DOWN"
            self.mob_start_point[1] -= vel_y
            
            
        elif self.move_down and self.mob_move_down:
            self.mirror_move = "UP"
            self.mob_start_point[1] += vel_y
            
            
        
        
        
    def draw(self):
        if not self.power_up_mob:
            if self.mob_move_left:
                self.mob = self.mob_0
            
            elif self.mob_move_right:
                self.mob = pygame.transform.flip(self.mob_0, True, False)
                
            else:
                self.mob = self.mob
            self.app.screen.blit(self.mob, (self.mob_start_point))
        elif self.power_up_mob:
            # self.mob = self.scared
            self.app.screen.blit(self.scared, (self.mob_start_point))
            
        
