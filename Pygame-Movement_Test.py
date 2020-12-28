import pygame
import math
pygame.init()
WIDTH, HIGH = 224*2, 288*2
screen = pygame.display.set_mode((WIDTH,HIGH))

# centro da figura: x + math.cos(math.pi/4)*r, y + x + math.sin(math.pi/4)*r

pygame.display.set_caption("Projeto Pac-Man")

x, y = 0,0        #posição inicial, posição pac man
raio = 25                      # raio
velx = 15  #ajustar velocidade!!
vely = 15

run = True     #main loop

while run:
    pygame.time.delay(100)
    
    
    for event in pygame.event.get(): #events
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    #movement pac_man
    if keys[pygame.K_LEFT] and x > velx:
        x -= velx
    if keys[pygame.K_RIGHT] and x - WIDTH < velx:
        x += velx
    if keys[pygame.K_UP]: #and y - math.cos(math.pi/4)*raio > vel:
        y -= vely
    if keys[pygame.K_DOWN]: #and y + 2 *raio  - HIGH < vel:
        y += vely
    
    # screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (255, 255, 0), (x, y), raio)
    pygame.display.update()
    
    
pygame.quit()