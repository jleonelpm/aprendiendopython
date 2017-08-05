import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

#Crea una superficie
ventana = pygame.display.set_mode((640,480))

pygame.display.set_caption("Animaciones")

imagen = pygame.image.load("imagenes/peppa.png")
posX = 100
posY = 100
pygame.mouse.set_pos(posX,posY)
velocidad = 10

blanco = (255,255,255)
izquierda = True
while True:
    ventana.fill(blanco)
    ventana.blit(imagen, (posX,posY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:    
            if evento.key == K_RIGHT:                
                if posX < 500:
                        posX += velocidad
            if evento.key == K_LEFT:                
                if posX>1:
                        posX -= velocidad
    ##Obtenemos la posicion del cursor
    posX, posY = pygame.mouse.get_pos()
    ## Esto nos sirve para centrar el cursor en la imagen
    posX = posX - 100
    posY = posY - 100
    
    pygame.display.update()