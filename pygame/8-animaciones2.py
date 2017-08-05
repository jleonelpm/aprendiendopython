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
                imagen = pygame.image.load("imagenes/george-der.png")
                if posX < 500:
                        posX += velocidad
            if evento.key == K_LEFT:
                imagen = pygame.image.load("imagenes/george-izq.png")
                if posX>1:
                        posX -= velocidad

    pygame.display.update()