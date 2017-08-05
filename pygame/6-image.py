import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

#Crea una superficie
ventana = pygame.display.set_mode((640,480))

pygame.display.set_caption("Imagenes")

imagen = pygame.image.load("imagenes/peppa.png")
posX = randint(10,300)
posY = randint(10,300)
ventana.blit(imagen, (posX,posY))

while True:
    //Permite resolver el problema de las imagenes
    ventana.fill(blanco)       

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:    
            if evento.key == K_ESCAPE:
                posX = randint(10,300)
                posY = randint(10,300)
                ventana.blit(imagen, (posX,posY))                
            if evento.key == K_0:
                    pygame.quit()
                    sys.exit()             
    pygame.display.update()