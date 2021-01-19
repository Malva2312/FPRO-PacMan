import pygame, sys
from settings import *
from Player import *

from Mob import *

import copy

pygame.init()
# vec = pygame.math.Vector2

class App:
    def __init__(self):
        
        
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.time = 0
        
        self.running = True
        self.state = "start"
        
        self.cell_width = MAZE_WIDTH/23.5789
        self.cell_height = MAZE_HEIGHT/25.255
       
        # self.map = MAZE_LIMITS
        # self.map_matrix = [list(x) for x in MAZE_LIMITS]
         
        self.move_up = False
        self.move_down = False
        self.move_left = True
        self.move_right = False
        
        
        
        self.high_score = 0
        
        self.load()
        
####################################################### MAIN_LOOP
    def run(self):
        while self.running:
            if self.state == "start":
                
                self.map_matrix = [list(x) for x in MAZE_LIMITS]
                self.score = 0
                
                self.start_events()
                self.start_update()
                self.start_draw()
                self.lifes = 3
                self.player =  Player(self, START_POINT.copy())
                
                self.blinky = Mob(self, MOB_START_POINT.copy(), "blinky.png")
                self.inky = Mob(self, INKY_START_POINT.copy(), "inky.png") 
                self.pinky = Mob(self, PINKY_START_POINT.copy(), "pinky.png") # MUDAR PARA PINKY START POINT
                self.clyde = Mob(self, CLYDE_START_POINT.copy(), "clyde.png" )
                
        
            elif self.state == "pregame":
                
                self.power_up = [False, 0]
                self.bonus = 0
                
                self.blinky.power_up_mob = False
                self.inky.power_up_mob = False
                self.pinky.power_up_mob = False
                self.clyde.power_up_mob = False
                
                self.player.start_point = START_POINT.copy()
                self.blinky.mob_start_point = MOB_START_POINT.copy()
                self.inky.mob_start_point = INKY_START_POINT.copy() 
                self.pinky.mob_start_point = PINKY_START_POINT.copy() # MUDAR PARA PINKY START POINT
                self.clyde.mob_start_point = CLYDE_START_POINT.copy()
                
                
                self.keys = pygame.key.get_pressed()
                self.pregame_events()
                self.pregame_update()
                self.pregame_draw()
                
                
            elif self.state == "playing":
                
                self.keys = pygame.key.get_pressed()
                self.playing_events()
                self.playing_update(self.map_matrix)
                self.playing_draw()
                
            elif self.state == "victory":
                self.victory_events()
                self.victory_update()
                self.victory_draw()
            
            elif self.state == "game over":
                    self.game_over_events()
                    self.game_over_update()
                    self.game_over_draw()
                    
            else:
                self.running = False
                
            # self.clock.tick(FPS)
            pygame.time.delay(20)    #????
        pygame.quit()
        sys.exit()
        
    
####################################################### DRAW
    def draw_lifes(self, lifes):
        if lifes == 3:
            self.screen.blit(self.n_lifes, ( TOP_BOT_BUFF , HEIGHT - TOP_BOT_BUFF/2))
            self.screen.blit(self.n_lifes, ( TOP_BOT_BUFF/2 , HEIGHT - TOP_BOT_BUFF/2))
        
        elif lifes == 2:
            self.screen.blit(self.n_lifes, ( TOP_BOT_BUFF/2 , HEIGHT - TOP_BOT_BUFF/2))
        else:
            pass


    def draw_some_text(self, astring, screen, position, size, colour, font_name, CENTER_WIDTH = True,CENTER_HEIGHT=True):
       font = pygame.font.SysFont(font_name, size) 
       text = font.render(astring, False, colour)
       text_size = text.get_size()
       #centering the sentence:
       if CENTER_HEIGHT:
           position[1] = position[1]-text_size[1]//2
       if CENTER_WIDTH:
            position[0] = position[0]-text_size[0]//2
       screen.blit(text, position)
    
    def load(self):
        self.background = pygame.image.load("PAC_MAN_MAZE.png")
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        
        self.n_lifes = pygame.image.load("pacman_mid2.png")
        self.n_lifes = pygame.transform.scale(self.n_lifes, (TOP_BOT_BUFF//2, TOP_BOT_BUFF//2))
    
    def draw_grid(self):
        for x in range(0, 19):
            pygame.draw.line(self.background, RED, (x*(WIDTH/((self.cell_width))), 0), (x*(WIDTH/(self.cell_width)), HEIGHT))
        
        for y in range(0, 21):
            pygame.draw.line(self.background, RED, (0, y*(HEIGHT/(self.cell_height))), (WIDTH, y*(HEIGHT/(self.cell_height))))
            
            
    def draw_points(self, a_matrix):
        
        for y in range(0, len(a_matrix)):
            for x in range(0, len(a_matrix[y])):
                if a_matrix[y][x] == 0:
                    pygame.draw.circle(self.screen, YELLOW, [x * MAZE_WIDTH/19 + MAZE_WIDTH/19/2 , y * MAZE_HEIGHT/21 + MAZE_HEIGHT/21/2 + TOP_BOT_BUFF/2], 3)



    def draw_big_points(self, a_matrix):
        for y in range(0, len(a_matrix)):
            for x in range(0, len(a_matrix[y])):
                if a_matrix[y][x] == 2:
                    pygame.draw.circle(self.screen, YELLOW, [x * MAZE_WIDTH/19 + MAZE_WIDTH/19/2 , y * MAZE_HEIGHT/21 + MAZE_HEIGHT/21/2 + TOP_BOT_BUFF/2], 7)

        

####################################################### MOVEMENT     
    def move(self,keys, vel_x, vel_y):
        self.player.matrix_pos(self.player.start_point)        
        
        if keys[pygame.K_LEFT] and self.player.move_left:
            self.move_up = False
            self.move_down = False
            self.move_left = True
            self.move_right = False
            
        elif keys[pygame.K_RIGHT] and self.player.move_right:
            self.move_up = False
            self.move_down = False
            self.move_left = False
            self.move_right = True
            
        elif keys[pygame.K_UP] and self.player.move_up:
            self.move_up = True
            self.move_down = False
            self.move_left = False
            self.move_right = False
            
        elif keys[pygame.K_DOWN] and self.player.move_down:
            self.move_up = False
            self.move_down = True
            self.move_left = False
            self.move_right = False
            
        
        if self.player.start_point[0]  < 0:
                self.move_up = False
                self.move_down = False
        
        if self.player.start_point[0] + DIAMETROx  > MAZE_WIDTH:
                self.move_up = False
                self.move_down = False
        
        
        if self.player.move_left and self.move_left:
            
            if self.player.start_point[0] - vel_x + DIAMETROx < 0:
                self.player.start_point[0] = MAZE_WIDTH - (self.player.start_point[0] + vel_x)
                
            else:
                self.player.start_point[0] -= vel_x
                    
                
                
                
        if self.move_right and self.player.move_right:
            
            if self.player.start_point[0] + vel_x  > MAZE_WIDTH:
                self.player.start_point[0] = MAZE_WIDTH - (self.player.start_point[0]  + DIAMETRO)
                
            else:
                self.player.start_point[0] += vel_x
            
            
            
        if self.move_up and self.player.move_up:
            
            self.player.start_point[1] -= vel_y
            
            
        if self.move_down and self.player.move_down:
            self.player.start_point[1] += vel_y
            
        
        if (self.player.move_left and self.move_left) or (self.move_right and self.player.move_right) or (self.move_up and self.player.move_up) or (self.move_down and self.player.move_down):
            
            self.player.animation_count+= 1
            if self.player.animation_count== 8:
                self.player.animation_count= 0
        else:
            self.player.animation_count = 0
            
####################################################### INTRODUCTION
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "pregame"
                
                
    def start_update(self):
        pass
    
    def start_draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_some_text("PRESS SPACE BAR",self.screen,[WIDTH//2, HEIGHT//2], TEXT_SIZE,ORANJE, START_SOURCE)
        pygame.display.update()
        
####################################################### PREGAME

    def pregame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT):
                self.state = "playing" 
                
                
    def pregame_update(self):
        pass
    
    def pregame_draw(self):
        self.screen.fill((0, 0, 0))
        
        
        # self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, TOP_BOT_BUFF/2))
        self.draw_some_text("READY!",self.screen,[WIDTH//2, HEIGHT//2 + MAZE_HEIGHT//21], TEXT_SIZE,YELLOW, START_SOURCE)
        # # self.draw_grid()
        self.draw_lifes(self.lifes)
        
        self.draw_some_text("HIGH SCORE:  {}".format(self.high_score), self.screen, [0, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=False) #HIGH SCORE MUST CHANGE
        self.draw_some_text("SCORE: {}".format(self.score), self.screen, [3/4 * WIDTH, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=True) #SCORE MUST CHANGE
        
        self.draw_points(self.map_matrix)
        self.draw_big_points(self.map_matrix)
        
        
        self.blinky.draw()
        self.inky.draw()
        self.pinky.draw()
        self.clyde.draw()
        
        self.player.draw()
        
        pygame.display.update()


####################################################### PLAYING
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        
        self.move(self.keys, vel_x, vel_y)
        
        
        
        
                
    def playing_update(self, a_matrix):
        
        
        if int((self.player.start_point[0]  ) // (MAZE_WIDTH/19)) > 0 and int((self.player.start_point[0] + DIAMETROx) // (MAZE_WIDTH/19)) < MAZE_WIDTH:
            if len(a_matrix) > int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21)):
                if len(a_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))]) > int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19)):
                    if a_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))][int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19))] == 0:
                        self.map_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))][int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19))] = 3
                        self.score += 10
                        
        if int((self.player.start_point[0]  ) // (MAZE_WIDTH/19)) > 0 and int((self.player.start_point[0] + DIAMETROx) // (MAZE_WIDTH/19)) < MAZE_WIDTH:
            if len(a_matrix) > int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21)):
                if len(a_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))]) > int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19)):
                    if a_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))][int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19))] == 2:
                        self.map_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))][int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19))] = 3
                        self.score += 50
                        self.power_up = [True, 0]
                        
                        self.blinky.power_up_mob = True
                        self.inky.power_up_mob = True
                        self.pinky.power_up_mob = True
                        self.clyde.power_up_mob = True
        
       # if self.map_matrix[int((self.blinky.mob_start_point[1] - TOP_BOT_BUFF/2 + MOB_DIAMETRO/2 )//(MAZE_HEIGHT/21))][int((self.mob.blinky_start_point[0] + MOB_DIAMETRO/2)//(MAZE_WIDTH/19))] ==5:

        if not self.power_up[0]:
            self.blinky.power_up_mob = False
            self.inky.power_up_mob = False
            self.pinky.power_up_mob = False
            self.clyde.power_up_mob = False
            
        if self.power_up[0]:
            t = self.clock.tick()
            self.power_up[1] += t
            
        if self.power_up[1] >= 7000:
            self.power_up = [False, 0]
            self.bonus = 0
            
        self.clock.tick()
        
        
        if not self.power_up[0]:
            self.blinky.power_up_mob = False
            self.inky.power_up_mob = False
            self.pinky.power_up_mob = False
            self.clyde.power_up_mob = False
        
        self.blinky.mob_colision()
        self.inky.mob_colision()
        self.pinky.mob_colision()
        self.clyde.mob_colision()
        
        if [x for y in a_matrix for x in y if x ==2 or x == 0] == []:
            self.state = "victory"
        
        
    
        
        
        if self.power_up[0]:
            self.clyde.move(mob_vel_x * (1/2), mob_vel_y * (1/2), self.player.start_point if self.power_up[0] == False else [(self.clyde.mob_start_point[0] - self.player.start_point[0]) + self.clyde.mob_start_point[0], (self.clyde.mob_start_point[1] - self.player.start_point[1]) + self.clyde.mob_start_point[1]]) #mudar goal
            self.pinky.move(mob_vel_x * (1/2), mob_vel_y * (1/2), self.player.start_point if self.power_up[0] == False else [(self.pinky.mob_start_point[0] - self.player.start_point[0]) + self.pinky.mob_start_point[0], (self.pinky.mob_start_point[1] - self.player.start_point[1]) + self.pinky.mob_start_point[1]]) #mudar goal
            self.inky.move(mob_vel_x * (1/2), mob_vel_y * (1/2), self.player.start_point if self.power_up[0] == False else [(self.inky.mob_start_point[0] - self.player.start_point[0]) + self.inky.mob_start_point[0], (self.inky.mob_start_point[1] - self.player.start_point[1]) + self.inky.mob_start_point[1]])
            self.blinky.move(mob_vel_x * (1/2), mob_vel_y * (1/2), self.player.start_point if self.power_up[0] == False else [(self.blinky.mob_start_point[0] - self.player.start_point[0]) + self.blinky.mob_start_point[0], (self.blinky.mob_start_point[1] - self.player.start_point[1]) + self.blinky.mob_start_point[1]])
        else:
            self.clyde.move(mob_vel_x , mob_vel_y , self.player.start_point if self.power_up[0] == False else [(self.clyde.inky_start_point[0] - self.player.start_point[0]) + self.clyde.mob_start_point[0], (self.clyde.mob_start_point[1] - self.player.start_point[1]) + self.clyde.inky_start_point[1]])
            self.pinky.move(mob_vel_x , mob_vel_y , self.player.start_point if self.power_up[0] == False else [(self.pinky.inky_start_point[0] - self.player.start_point[0]) + self.pinky.mob_start_point[0], (self.pinky.mob_start_point[1] - self.player.start_point[1]) + self.pinky.inky_start_point[1]]) #mudar goal
            self.inky.move(mob_vel_x , mob_vel_y , self.player.start_point if self.power_up[0] == False else [(self.inky.inky_start_point[0] - self.player.start_point[0]) + self.inky.mob_start_point[0], (self.inky.mob_start_point[1] - self.player.start_point[1]) + self.inky.inky_start_point[1]])
            self.blinky.move(mob_vel_x, mob_vel_y, self.player.start_point if self.power_up[0] == False else [(self.blinky.mob_start_point[0] - self.player.start_point[0]) + self.blinky.mob_start_point[0], (self.blinky.mob_start_point[1] - self.player.start_point[1]) + self.blinky.mob_start_point[1]])
        
        
    
    def playing_draw(self):
        
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, TOP_BOT_BUFF/2))
        # self.draw_grid()
        
        self.draw_lifes(self.lifes)
        
        self.draw_some_text("HIGH SCORE:  {}".format(self.high_score), self.screen, [0, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=False) #HIGH SCORE MUST CHANGE
        self.draw_some_text("SCORE: {}".format(self.score), self.screen, [3/4 * WIDTH, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=True) #SCORE MUST CHANGE
        
        self.draw_points(self.map_matrix)
        self.draw_big_points(self.map_matrix)
        
        
        self.blinky.draw()
        self.inky.draw()
        self.pinky.draw()
        self.clyde.draw()
        
        self.player.draw()
        
        
        pygame.display.update()
        
########################################################################################## GAME OVER
    def game_over_events(self):
        if self.score > self.high_score:
            self.high_score = self.score
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN: #and event.key == pygame.K_SPACE:
                self.state = "start"
                
                
    def game_over_update(self):
        pass
    
    def game_over_draw(self):
        self.screen.fill((0, 0, 0))
        
        
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, TOP_BOT_BUFF/2))
        self.draw_some_text("GAME OVER!",self.screen,[WIDTH//2, HEIGHT//2 + MAZE_HEIGHT//21], TEXT_SIZE,RED, START_SOURCE)
        
        self.draw_some_text("HIGH SCORE:  {}".format(self.high_score), self.screen, [0, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=False) #HIGH SCORE MUST CHANGE
        self.draw_some_text("SCORE: {}".format(self.score), self.screen, [3/4 * WIDTH, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=True) #SCORE MUST CHANGE
        
        
        pygame.display.update()
        
############################################################################# VICTORY
    def victory_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "start"
                
                
    def victory_update(self):
        if self.score > self.high_score:
            self.high_score = self.score
    
    def victory_draw(self):
        self.screen.fill((0, 0, 0))
        
        
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, TOP_BOT_BUFF/2))
        self.draw_some_text("CONGRATULATIONS!",self.screen,[WIDTH//2, HEIGHT//2 + MAZE_HEIGHT//21], TEXT_SIZE,YELLOW, START_SOURCE)
        
        self.draw_some_text("HIGH SCORE:  {}".format(self.high_score), self.screen, [0, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=False) #HIGH SCORE MUST CHANGE
        self.draw_some_text("SCORE: {}".format(self.score), self.screen, [3/4 * WIDTH, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=True) #SCORE MUST CHANGE
        
        
        pygame.display.update()
        
####################################################################################
app = App()
app.run()