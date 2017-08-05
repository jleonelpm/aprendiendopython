import pygame,sys
from pygame.locals import *

ColorUno = (0,140,60)
ColorDos = pygame.Color(200,200,56)

pygame.init()

#Retorna una superficie
ventana = pygame.display.set_mode((400,300))

pygame.display.set_caption("hola Mundo")
pygame.draw.line(ventana, ColorUno, (60,80), (160,160), 1)
while True:
    ventana.fill(ColorDos)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()