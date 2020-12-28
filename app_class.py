import pygame, sys
from settings import *
from Player import *

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
        # self.x, self.y= MAZE_WIDTH/2, MAZE_HEIGHT/2 + MAZE_HEIGHT/21
        # self.xvel, self.yvel = MAZE_WIDTH/19, MAZE_HEIGHT/21
        self.player =  Player(self, START_POINT)
        
        self.load()
        
####################################################### MAIN_LOOP
    def run(self):
        while self.running:
            if self.state == "start":
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
                
            self.clock.tick(FPS)
            # pygame.time.delay(188)    #????
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
        self.draw_some_text("PRESS SPACE BAR",self.screen,[WIDTH//2, HEIGHT//2], TEXT_SIZE,(240, 134, 37), START_SOURCE) #(240, 134, 37)== orange
        pygame.display.update()
        

####################################################### PLAYING
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:# and (self.player.start_point[0] + RADIOS - vel >2* cell):
            self.player.start_point[0] -= vel
        if self.keys[pygame.K_RIGHT]:# and (self.player.start_point[0] + RADIOS + vel < MAZE_WIDTH - MAZE_WIDTH/19):
            self.player.start_point[0] += vel
        if self.keys[pygame.K_UP]:
            self.player.start_point[1] -= vel
        if self.keys[pygame.K_DOWN]:
            self.player.start_point[1] += vel
                
    def playing_update(self):
        pass
    
    def playing_draw(self):
        self.screen.blit(self.background, (0, TOP_BOT_BUFF/2))
        self.draw_grid()
        self.draw_some_text("HIGH SCORE: {}".format("0 for now"), self.screen, [0, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=False) #HIGH SCORE MUST CHANGE
        self.draw_some_text("SCORE: {}".format("0 for now"), self.screen, [3/4 * WIDTH, 0], 16, WHITE , START_SOURCE, CENTER_HEIGHT=False, CENTER_WIDTH=True) #SCORE MUST CHANGE
        self.player.draw()
        
        pygame.display.update()
        
        
app = App()
app.run()