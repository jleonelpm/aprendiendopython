import pygame,sys
from pygame.locals import *

pygame.init()

#Retorna una superficie
ventana = pygame.display.set_mode((600,480))

pygame.display.set_caption("Uso de Fonts")

miFuente = pygame.font.Font("fonts/Sketch3D.otf", 60)
color = (255,195,0)
miTexto = miFuente.render("Aluxin Games",0,color)

miFuente2 = pygame.font.SysFont("Arial", 40)
color = (199,0,157)
miTexto2 = miFuente2.render("Derechos Reservados",0,color)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    ventana.blit(miTexto,(10,100))
    ventana.blit(miTexto2,(10,200))
    pygame.display.update()