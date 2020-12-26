import pygame
import math
pygame.init()
WIDTH, HIGH = 224*2, 288*2
screen = pygame.display.set_mode((WIDTH,HIGH))

# centro da figura: x + math.cos(math.pi/4)*r, y + x + math.sin(math.pi/4)*r

pygame.display.set_caption("Projeto Pac-Man")

x, y = 50, 50             #posição inicial, posição pac man
raio = 15                         # raio
vel = 10  #ajustar velocidade!!


run = True     #main loop

while run:
    pygame.time.delay(100)
    
    
    for event in pygame.event.get(): #events
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    #movement pac_man
    if keys[pygame.K_LEFT] and (x - math.cos(math.pi/4)*raio > vel):
        x -= vel
    if keys[pygame.K_RIGHT] and x + 2 *raio  - WIDTH < vel:
        x += vel
    if keys[pygame.K_UP] and y - math.cos(math.pi/4)*raio > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y + 2 *raio  - HIGH < vel:
        y += vel
    
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (255, 255, 0), (x, y), raio)
    pygame.display.update()
    
    
pygame.quit()