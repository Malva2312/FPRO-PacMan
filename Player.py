import pygame
import math
from pygame.math import Vector2 as vec
from settings import *

    
class Player:
    def __init__(self, app, point):
        self.app = app
        self.start_point = point
        
        self.load()
        
    def update(self):
        pass
    
    def draw(self):
        self.app.screen.blit(self.pac_man, (self.start_point))
    
        
    def load(self):
        self.pac_man = pygame.image.load("pacman_fill.png")
        self.pac_man = pygame.transform.scale(self.pac_man, (RADIOS, RADIOS))