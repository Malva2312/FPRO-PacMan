import pygame
import math
from settings import *
import random
                    

class INKY:
    def __init__(self, app, point):  #, Color
        self.app = app
        self.inky_start_point = point
        self.center = [point[0] + RADIOS, point[1] + RADIOS -  TOP_BOT_BUFF]
        
        
        self.inky_move_up = False
        self.inky_move_down = False
        self.inky_move_left = False
        self.inky_move_right = False
        
        
        self.app = app
        
        
        self.count = 0
        
        self.load()
        
    
    
    def load(self):
        
        self.inky = pygame.image.load("inky.png")
        self.inky = pygame.transform.flip(self.inky, True, False)
        
        self.inky = pygame.transform.scale(self.inky, (MOB_DIAMETROx, MOB_DIAMETRO))
        self.inky_0 = self.inky
        
        self.scared = pygame.image.load("scared ghost.png")
        self.scared = pygame.transform.scale(self.scared, (MOB_DIAMETROx, MOB_DIAMETRO))
    
    def matrix_pos(self,position):
        
        if [(self.inky_start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.inky_start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.inky_start_point[0] + DIAMETROx + vel_x)//(MAZE_WIDTH/19), (self.inky_start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS :
            
            self.move_right = False
        else:
            self.move_right = True
        
        if [(self.inky_start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.inky_start_point[1] - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.inky_start_point[0] - vel_x)//(MAZE_WIDTH/19), (self.inky_start_point[1] + DIAMETRO - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)] in MOB_BLOCKS :
            
            self.move_left = False
        else:
            self.move_left = True
        
        if [self.inky_start_point[0]//(MAZE_WIDTH/19), (self.inky_start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.inky_start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.inky_start_point[1] - TOP_BOT_BUFF/2 + vel_y + DIAMETRO)//(MAZE_HEIGHT/21)] in MOB_BLOCKS:
            
            self.move_down = False
        else:
            self.move_down = True
            
        if [self.inky_start_point[0]//(MAZE_WIDTH/19), (self.inky_start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in MOB_BLOCKS or [(self.inky_start_point[0] + DIAMETROx)//(MAZE_WIDTH/19), (self.inky_start_point[1] - TOP_BOT_BUFF/2 - vel_y)//(MAZE_HEIGHT/21)] in MOB_BLOCKS:
            
            self.move_up = False
        else:
            self.move_up = True
            

  
    
  
    
    def next_move(self, goal, absolute_pos, blocks):
            
        queue = []
        
        
        
        pos = queue[0]
        queue.pop(0)
        
        count = 0
        
        while goal != pos[0] :
            
            count += 1
            
            pos = queue[0]
            matrix_pos = pos[0]
            queue.pop(0)
            
            if not [matrix_pos[0], matrix_pos[1] -1] in blocks + pos[1]:
                queue.append(([matrix_pos[0], matrix_pos[1] - 1], matrix_pos + pos[1], pos[2]))
            
            if not [matrix_pos[0], matrix_pos[1] + 1] in blocks + pos[1]:
                queue.append(([matrix_pos[0], matrix_pos[1] + 1], matrix_pos + pos[1], pos[2]))
            
            if not [matrix_pos[0] + 1, matrix_pos[1]] in blocks + pos[1]:
                queue.append(([matrix_pos[0] +1 , matrix_pos[1]], matrix_pos + pos[1], pos[2]))
            
            if not [matrix_pos[0] - 1, matrix_pos[1]] in blocks + pos[1]:
                queue.append(([matrix_pos[0] - 1 , matrix_pos[1]], matrix_pos + pos[1], pos[2]))
                
        
        self.move_direction = pos[2]
    
    
    def move(self, vel_x, vel_y, goal):
        self.matrix_pos(self.inky_start_point)        
        
        
        X, Y = abs(goal[0] - self.inky_start_point[0]),  abs(goal[1] - self.inky_start_point[1])
        
        ABSx = abs( goal[0] - self.inky_start_point[0]) > 1
        ABSy = abs(  goal[1] - self.inky_start_point[1] ) > 1
        
        
        
        
        
################################################################################    

        # goal = [(goal[0] + DIAMETROx/2 + vel_x)//(MAZE_WIDTH/19), (goal[1] + DIAMETRO/2 - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)]
        # # goal = [18, 1]
        # move = self.next_move(goal,self.inky_start_point, BLOCKS_POS) #BLOCKS_POS
        
        # if self.move_direction == "UP" :
        #     self.inky_move_up = True
        #     self.inky_move_down = False
        #     self.inky_move_left = False
        #     self.inky_move_right = False
        
        # elif self.move_direction == "DOWN" :
        #     self.inky_move_up = False
        #     self.inky_move_down = True
        #     self.inky_move_left = False
        #     self.inky_move_right = False
        
        # elif self.move_direction == "LEFT" :
        #     self.inky_move_up = False
        #     self.inky_move_down = False
        #     self.inky_move_left = True
        #     self.inky_move_right = False
            
        # elif self.move_direction == "RIGHT" :
        #     self.inky_move_up = False
        #     self.inky_move_down = False
        #     self.inky_move_left = False
        #     self.inky_move_right = True

################################################################################
############################################################################## BASIC MOVEMENT INSTROTIONS
        
        if self.count == 0:
            if X >= Y:
                if (goal[0] < self.inky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = True
                    self.inky_move_right = False
                    
                elif goal[0] > self.inky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = True
                    
                elif goal[1] < self.inky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.inky_move_up = True
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = False
                    
                    
                elif goal[1] > self.inky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.inky_move_up = False
                    self.inky_move_down = True
                    self.inky_move_left = False
                    self.inky_move_right = False
                
                
            
                else:
                    self.count = 1
                    
            elif Y >= X:
                if goal[1] < self.inky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.inky_move_up = True
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = False
                    
                    
                elif goal[1] > self.inky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.inky_move_up = False
                    self.inky_move_down = True
                    self.inky_move_left = False
                    self.inky_move_right = False
                
                elif (goal[0] < self.inky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = True
                    self.inky_move_right = False
                    
                elif goal[0] > self.inky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = True
                
                else:
                    self.count = 1
                    
                    

############################################################################## RANDOM LOGIC                    

        else:
            ############ if stuck: random logic##############
            # path = list(filter())
            
            
            
            # random.shuffle(PATH)
            pos = [0, 0]
            pos[0] = (self.inky_start_point[0] - goal[0]) + self.inky_start_point[0]
            pos[1] = (self.inky_start_point[1] - goal[1]) + self.inky_start_point[1]
            
            # print(pos)                                                 # improve the random logic
            
            X, Y = abs(pos[0] - self.inky_start_point[0]),  abs(pos[1] - self.inky_start_point[1])
        
            ABSx = abs( pos[0] - self.inky_start_point[0]) > 1
            ABSy = abs(  pos[1] - self.inky_start_point[1] ) > 1
            
            
            if X >= Y:
                if (pos[0] < self.inky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = True
                    self.inky_move_right = False
                    
                elif pos[0] > self.inky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = True
                    
                elif pos[1] < self.inky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.inky_move_up = True
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = False
                    
                    
                elif pos[1] > self.inky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.inky_move_up = False
                    self.inky_move_down = True
                    self.inky_move_left = False
                    self.inky_move_right = False
            
                
            
                    
            elif Y >= X:
                if pos[1] < self.inky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.inky_move_up = True
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = False
                    
                    
                elif pos[1] > self.inky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.inky_move_up = False
                    self.inky_move_down = True
                    self.inky_move_left = False
                    self.inky_move_right = False
                
                elif (pos[0] < self.inky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = True
                    self.inky_move_right = False
                    
                elif pos[0] > self.inky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.inky_move_up = False
                    self.inky_move_down = False
                    self.inky_move_left = False
                    self.inky_move_right = True
            
            self.count += 1
            if self.count == 16 * 8:
                self.count = 0
            
################################################################################     
        
################################################################################    
    


################################################################################
            # if self.count % 8 == 0:
                
                    
                    
            #         if self.move_up and self.move_down and self.move_left and self.move_right:
                        
            #             a = random.randint(0,3)
                        
            #             if a == 0:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = True
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = True
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 2:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = True
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 3:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = True
                        
                        
                        
                        
            #         elif self.move_up and self.move_down and self.move_right:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.inky_move_up = True
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = True
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 2:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = True
                        
                        
            #         elif self.move_up and self.move_down and self.move_left:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = True
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = True
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 2:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = True
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
                    
                    
                    
                    
            #         elif self.move_up and self.move_left and self.move_right:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = True
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = True
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 2:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = True
                    
                    
                    
                    
            #         elif self.move_down and self.move_left and self.move_right:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = True
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = True
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 2:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = True
                            
                    
            #         elif self.move_up and self.move_down:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.inky_move_up = True
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = True
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
                        
                        
                    
            #         elif self.move_up and self.move_right:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.inky_move_up = True
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = True
                    
                    
            #         elif self.move_up and self.move_left:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.inky_move_up = True
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = True
            #                 self.inky_move_right = False
                            
                    
            #         elif self.move_down and self.move_right:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = True
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = True
                    
                    
            #         elif self.move_down and self.move_left:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = True
            #                 self.inky_move_left = False
            #                 self.inky_move_right = False
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = True
            #                 self.inky_move_right = False
                    
                    
            #         elif self.move_right and self.move_left:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = False
            #                 self.inky_move_right = True
            #             elif a == 1:
            #                 self.inky_move_up = False
            #                 self.inky_move_down = False
            #                 self.inky_move_left = True
            #                 self.inky_move_right = False
        
        
        # elif not( (goal[0] < self.inky_start_point[0] and self.move_left) or (goal[0] > self.inky_start_point[0] and self.move_right) or (goal[1] < self.inky_start_point[1] and self.move_up) or (goal[1] > self.inky_start_point[1] and self.move_down)  ):
        #     None
            
            
############################################################################## OUT OF MAZE LMITS
        
        if self.inky_start_point[0]  - MAZE_WIDTH/19 + 1< 0:
                self.inky_move_up = False
                self.inky_move_down = False
                self.inky_move_right = False
                self.inky_move_left = True
        
        if self.inky_start_point[0] +  MOB_DIAMETROx + MAZE_WIDTH/19 -1 > MAZE_WIDTH:
                self.inky_move_up = False
                self.inky_move_down = False
                self.inky_move_right = False
                self.inky_move_left = True
        
        # 330.9342105263149
        # 96.0657894736841
        # print(self.inky_start_point)
        
   ###################### MOVEMENT CALCULATION ##############################     
        if self.inky_move_left and self.move_left:
            
            if self.inky_start_point[0] - vel_x + DIAMETROx < 0:
                self.inky_start_point[0] = MAZE_WIDTH - (self.inky_start_point[0] + vel_x)
                
            else:
                self.inky_start_point[0] -= vel_x
                    
                
        elif self.move_right and self.inky_move_right:
            
            if self.inky_start_point[0] + vel_x  > MAZE_WIDTH:
                self.inky_start_point[0] = MAZE_WIDTH - (self.inky_start_point[0]  + DIAMETRO)
                
            else:
                self.inky_start_point[0] += vel_x
            
            
        elif self.move_up and self.inky_move_up:
            
            self.inky_start_point[1] -= vel_y
            
            
        elif self.move_down and self.inky_move_down:
            self.inky_start_point[1] += vel_y
            
            
        # print((self.inky__left and self.move_left) or (self.move_right and self.inky__right) or (self.move_up and self.inky__up) or (self.move_down and self.inky__down))
        # print(self.inky_move_up ,self.inky_move_down, self.inky_move_left, self.inky_move_right)
        # print("up", self.inky_move_up, self.move_up)
        # print("down", self.inky_move_down, self.move_down)
        # print("left", self.inky_move_left, self.move_left)
        # print("right", self.inky_move_right, self.move_right)
        
        
        
    def draw(self):
        if not self.app.power_up[0]:
            if self.inky_move_left:
                self.inky = self.inky_0
            
            elif self.inky_move_right:
                self.inky = pygame.transform.flip(self.inky_0, True, False)
                
            else:
                self.inky = self.inky
        else:
            self.inky = self.scared
        self.app.screen.blit(self.inky, (self.inky_start_point))