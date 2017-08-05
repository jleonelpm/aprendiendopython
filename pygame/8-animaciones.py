import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

#Crea una superficie
ventana = pygame.display.set_mode((640,480))

pygame.display.set_caption("Animaciones")

imagen = pygame.image.load("imagenes/george-der.png")
posX = 10
posY = 100
velocidad = 1

blanco = (255,255,255)
izquierda = True
while True:
    ventana.fill(blanco)
    ventana.blit(imagen, (posX,posY))
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    #Este codigo permite generar el movimiento
    #De izquierda a derecha
    if izquierda==True:
        if posX < 500:
            posX += velocidad
        else:
            izquierda = False
            imagen = pygame.image.load("imagenes/george-izq.png")
    else:
        if posX>1:
            posX -= velocidad
        else:
            izquierda = True
            imagen = pygame.image.load("imagenes/george-der.png")


    pygame.display.update()