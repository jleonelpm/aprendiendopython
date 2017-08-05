import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

#Crea una superficie
ventana = pygame.display.set_mode((640,480))

pygame.display.set_caption("Colisiones")

#imagen = pygame.image.load("imagenes/peppa.png")
posX = 100
posY = 100
velocidad = 1

blanco = (255,255,255)
azul = (45,56,231)
naranja = (249, 63, 4)
izquierda = True

rectangulo = pygame.Rect(0,0,100,150)
rectangulo_dos = pygame.Rect(300,300,100,50)
while True:
    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, rectangulo_dos)
    pygame.draw.rect(ventana, naranja, rectangulo)
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()

    ##Aqui se detecta la colision
    if rectangulo.colliderect(rectangulo_dos):
        velocidad = 0

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    if izquierda==True:
        if posX < 500:
            posX += velocidad
            rectangulo_dos.left = posX
        else:
            izquierda = False

    else:
        if posX>1:
            posX -= velocidad
            rectangulo_dos.left = posX
        else:
            izquierda = True

    pygame.display.update()