import pygame,sys
from pygame.locals import *

ColorUno = (0,140,60)
ColorDos = pygame.Color(200,200,56)
ColorTres = pygame.Color(255,200,100)

pygame.init()

#Retorna una superficie
ventana = pygame.display.set_mode((640,480))

pygame.display.set_caption("hola Mundo")
pygame.draw.line(ventana, ColorUno, (60,80), (160,160), 3)
pygame.draw.line(ventana, ColorDos, (160,160), (300,120), 3)
pygame.draw.line(ventana, ColorTres, (300,120), (60,80), 3)

while True:
    #ventana.fill(ColorDos)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()