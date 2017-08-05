import pygame,sys
from pygame.locals import *

pygame.init()

#Retorna una superficie
ventana = pygame.display.set_mode((600,480))

pygame.display.set_caption("Uso del Timer")

miFuente = pygame.font.Font("fonts/SuperMario256.ttf", 60)
color = (255,195,0)

aux = 1

while True:
    ventana.fill((255,255,255))

    # Se obtiene el tiempo en milisegundos a partir del cual
    # init() fue iniciado, se divide entre 1000 para convertir a segundos
    Tiempo = pygame.time.get_ticks()/1000

    if aux == Tiempo:
        aux += 1
        
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    miTexto = miFuente.render("Tiempo " + str(Tiempo),0,color)

    ventana.blit(miTexto,(10,100))
    
    pygame.display.update()