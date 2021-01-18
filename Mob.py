import pygame
import math
from settings import *
import random
                    
# def next_move(goal, absolute_pos, blocks):
            
            
#             matrix_pos = [(absolute_pos[0]+ MOB_DIAMETROx/2) // (MAZE_WIDTH/19), (absolute_pos[1] + DIAMETRO/2 - TOP_BOT_BUFF)// (MAZE_HEIGHT/21)]
#             queue = [[matrix_pos, [], None]]  #pos + blocks + direction  
            
#             pos = queue[0]
            
#             count = 0
            
            
#             while goal != pos[0] or count ==50:
                
#                 queue.pop(0)
            
            
#                 if move_up and not [matrix_pos[0], matrix_pos[1] -1] in blocks + pos[1]:
#                     if pos[2] == None:
#                         queue.append([[matrix_pos[0], matrix_pos[1] -1], pos, "UP"])
#                     else:
#                         queue.append([[matrix_pos[0], matrix_pos[1] -1], pos[0], pos[2]])
                    
#                     count += 1
                
#                 if move_down and not [matrix_pos[0], matrix_pos[1] + 1] in blocks + pos[1]:
#                     if pos[2] == None:
#                         queue.append([[matrix_pos[0], matrix_pos[1] + 1], pos[0], "DOWN"])
#                     else:
#                         queue.append([[matrix_pos[0], matrix_pos[1] + 1], pos[0], pos[2]])
                    
#                     count +=1
                    
#                 if move_left and not [matrix_pos[0]-1, matrix_pos[1]] in blocks + pos[1]:
#                     if pos[2] == None:
#                         queue.append([[matrix_pos[0]-1, matrix_pos[1], pos], pos, "LEFT"])
#                     else:
#                         queue.append([[matrix_pos[0]-1, matrix_pos[1], pos], pos, pos[2]])
                        
#                     count += 1
                    
#                 if move_right and not [matrix_pos[0]+1, matrix_pos[1]] in blocks + pos[1]:
#                     if pos[2] == None:
#                         queue.append([[matrix_pos[0]+1, matrix_pos[1]], pos, "RIGHT"])
#                     else:
#                         queue.append([[matrix_pos[0]+1, matrix_pos[1]], pos, pos[2]])
                    
#                     count +=1 
                    
                    
                    
#                 pos = queue[0]
                
#             return pos[2]




class Mob:
    def __init__(self, app, point):  #, Color
        self.app = app
        self.blinky_start_point = point
        self.center = [point[0] + RADIOS, point[1] + RADIOS -  TOP_BOT_BUFF]
        
        
        self.blinky_move_up = False
        self.blinky_move_down = False
        self.blinky_move_left = False
        self.blinky_move_right = False
        
        
        self.app = app
        
        
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
    
    
    def move(self, vel_x, vel_y):
        self.matrix_pos(self.blinky_start_point)        
        
        
        X, Y = abs(self.app.player.start_point[0] - self.blinky_start_point[0]),  abs(self.app.player.start_point[1] - self.blinky_start_point[1])
        
        ABSx = abs( self.app.player.start_point[0] - self.blinky_start_point[0]) > 1
        ABSy = abs(  self.app.player.start_point[1] - self.blinky_start_point[1] ) > 1
        
        
        
        
        
################################################################################    

        # goal = [(self.app.player.start_point[0] + DIAMETROx/2 + vel_x)//(MAZE_WIDTH/19), (self.app.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2)//(MAZE_HEIGHT/21)]
        # # goal = [18, 1]
        # move = self.next_move(goal,self.blinky_start_point, BLOCKS_POS) #BLOCKS_POS
        
        # if self.move_direction == "UP" :
        #     self.blinky_move_up = True
        #     self.blinky_move_down = False
        #     self.blinky_move_left = False
        #     self.blinky_move_right = False
        
        # elif self.move_direction == "DOWN" :
        #     self.blinky_move_up = False
        #     self.blinky_move_down = True
        #     self.blinky_move_left = False
        #     self.blinky_move_right = False
        
        # elif self.move_direction == "LEFT" :
        #     self.blinky_move_up = False
        #     self.blinky_move_down = False
        #     self.blinky_move_left = True
        #     self.blinky_move_right = False
            
        # elif self.move_direction == "RIGHT" :
        #     self.blinky_move_up = False
        #     self.blinky_move_down = False
        #     self.blinky_move_left = False
        #     self.blinky_move_right = True

################################################################################
############################################################################## BASIC MOVEMENT INSTROTIONS
        
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
                    
                    

############################################################################## RANDOM LOGIC                    

        else:
            ############ if stuck: random logic##############
            # path = list(filter())
            
            
            
            # random.shuffle(PATH)
            pos = [0, 0]
            pos[0] = (self.blinky_start_point[0] - self.app.player.start_point[0]) + self.blinky_start_point[0]
            pos[1] = (self.blinky_start_point[1] - self.app.player.start_point[1]) + self.blinky_start_point[1]
            
            # print(pos)                                                 # improve the random logic
            
            X, Y = abs(pos[0] - self.blinky_start_point[0]),  abs(pos[1] - self.blinky_start_point[1])
        
            ABSx = abs( pos[0] - self.blinky_start_point[0]) > 1
            ABSy = abs(  pos[1] - self.blinky_start_point[1] ) > 1
            
            
            if X >= Y:
                if (pos[0] < self.blinky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = True
                    self.blinky_move_right = False
                    
                elif pos[0] > self.blinky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = True
                    
                elif pos[1] < self.blinky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.blinky_move_up = True
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = False
                    
                    
                elif pos[1] > self.blinky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.blinky_move_up = False
                    self.blinky_move_down = True
                    self.blinky_move_left = False
                    self.blinky_move_right = False
            
                
            
                    
            elif Y >= X:
                if pos[1] < self.blinky_start_point[1] and self.move_up and ABSy:  #  and Y>X:
                    self.blinky_move_up = True
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = False
                    
                    
                elif pos[1] > self.blinky_start_point[1] and self.move_down and ABSy: # and Y>X:
                    self.blinky_move_up = False
                    self.blinky_move_down = True
                    self.blinky_move_left = False
                    self.blinky_move_right = False
                
                elif (pos[0] < self.blinky_start_point[0] and self.move_left) and ABSx:    # or X > Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = True
                    self.blinky_move_right = False
                    
                elif pos[0] > self.blinky_start_point[0] and self.move_right and ABSx: # and X>Y:
                    self.blinky_move_up = False
                    self.blinky_move_down = False
                    self.blinky_move_left = False
                    self.blinky_move_right = True
            
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
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = True
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = True
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 2:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = True
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 3:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = True
                        
                        
                        
                        
            #         elif self.move_up and self.move_down and self.move_right:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.blinky_move_up = True
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = True
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 2:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = True
                        
                        
            #         elif self.move_up and self.move_down and self.move_left:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = True
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = True
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 2:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = True
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
                    
                    
                    
                    
            #         elif self.move_up and self.move_left and self.move_right:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = True
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = True
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 2:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = True
                    
                    
                    
                    
            #         elif self.move_down and self.move_left and self.move_right:
                        
            #             a = random.randint(0,2)
                        
            #             if a == 0:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = True
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = True
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 2:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = True
                            
                    
            #         elif self.move_up and self.move_down:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.blinky_move_up = True
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = True
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
                        
                        
                    
            #         elif self.move_up and self.move_right:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.blinky_move_up = True
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = True
                    
                    
            #         elif self.move_up and self.move_left:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.blinky_move_up = True
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = True
            #                 self.blinky_move_right = False
                            
                    
            #         elif self.move_down and self.move_right:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = True
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = True
                    
                    
            #         elif self.move_down and self.move_left:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = True
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = False
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = True
            #                 self.blinky_move_right = False
                    
                    
            #         elif self.move_right and self.move_left:
            #             a = random.randint(0,1)
            #             if a == 0:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = False
            #                 self.blinky_move_right = True
            #             elif a == 1:
            #                 self.blinky_move_up = False
            #                 self.blinky_move_down = False
            #                 self.blinky_move_left = True
            #                 self.blinky_move_right = False
        
        
        # elif not( (self.app.player.start_point[0] < self.blinky_start_point[0] and self.move_left) or (self.app.player.start_point[0] > self.blinky_start_point[0] and self.move_right) or (self.app.player.start_point[1] < self.blinky_start_point[1] and self.move_up) or (self.app.player.start_point[1] > self.blinky_start_point[1] and self.move_down)  ):
        #     None
            
            
############################################################################## OUT OF MAZE LMITS
        
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
        
        
   ###################### MOVEMENT CALCULATION ##############################     
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
            
        
