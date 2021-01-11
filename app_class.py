import pygame, sys
from settings import *
from Player import *
from Mob import *

pygame.init()
# vec = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "start"
        
        self.cell_width = MAZE_WIDTH/23.5789
        self.cell_height = MAZE_HEIGHT/25.255
        
        self.player =  Player(self, START_POINT)
        self.mob = Mob(self, MOB_START_POINT)
        
        self.map_matrix = MAZE_LIMITS
        
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        
        # self.player.animation_count = 0
        
        self.score = 0
        
        self.load()
        
####################################################### MAIN_LOOP
    def run(self):
        while self.running:
            if self.state == "start":
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == "playing":
                self.keys = pygame.key.get_pressed()
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
                
            # self.clock.tick(FPS)
            pygame.time.delay(20)    #????
        pygame.quit()
        sys.exit()
        
    
####################################################### DRAW
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
        
        
        # 330.9342105263149
        # 96.0657894736841
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
            
        # print((self.player.move_left and self.move_left) or (self.move_right and self.player.move_right) or (self.move_up and self.player.move_up) or (self.move_down and self.player.move_down))
        
        if (self.player.move_left and self.move_left) or (self.move_right and self.player.move_right) or (self.move_up and self.player.move_up) or (self.move_down and self.player.move_down):
            
            self.player.animation_count+= 1
            if self.player.animation_count== 8:
                self.player.animation_count= 0
        else:
            self.player.animation_count = 0
            
        # print(self.player.animation_count)
####################################################### INTRODUCTION
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "playing"
                
                
    def start_update(self):
        pass
    
    def start_draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_some_text("PRESS SPACE BAR",self.screen,[WIDTH//2, HEIGHT//2], TEXT_SIZE,ORANJE, START_SOURCE)
        pygame.display.update()
        

####################################################### PLAYING
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        
        self.move(self.keys, vel_x, vel_y)
        
                
    def playing_update(self):
        
        
        if int((self.player.start_point[0]  ) // (MAZE_WIDTH/19)) > 0 and int((self.player.start_point[0] + DIAMETROx) // (MAZE_WIDTH/19)) < MAZE_WIDTH:
            if len(self.map_matrix) > int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21)):
                if len(self.map_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))]) > int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19)):
                    if self.map_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))][int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19))] == 0:
                        self.map_matrix[int((self.player.start_point[1] + DIAMETRO/2 - TOP_BOT_BUFF/2) // (MAZE_HEIGHT/21))][int((self.player.start_point[0] + RADIOS) // (MAZE_WIDTH/19))] = 3
                        self.score += 10
        
        self.mob.move(mob_vel_x, mob_vel_y)
        
    
    def playing_draw(self):
        
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, TOP_BOT_BUFF/2))
        # self.draw_grid()
        
        self.draw_some_text("HIGH SCORE:  {}".format(self.score), self.screen, [0, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=False) #HIGH SCORE MUST CHANGE
        self.draw_some_text("SCORE: {}".format("0 for now"), self.screen, [3/4 * WIDTH, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=True) #SCORE MUST CHANGE
        
        self.draw_points(self.map_matrix)
        self.draw_big_points(self.map_matrix)
        
        
        self.mob.draw()
        self.player.draw()
        
        
        
        
        # print(self.player.start_point, self.mob.blinky_start_point)
        
        pygame.display.update()
        
####################################################### 
    
        
        

####################################################### 
app = App()
app.run()