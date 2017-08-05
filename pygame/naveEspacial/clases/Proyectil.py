import pygame,sys
from pygame.locals import *
#La clase Proyectil
#hereda a partir de la clase Sprite de pygame
class Proyectil(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, posX, posY, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)
        #dependiendo del objeto es la ruta de la imagen a cargar
        self.Img = pygame.image.load(ruta)

        #Se asigna a la imagen un rectangulo
        self.rect = self.Img.get_rect()
        self.velocidadDisparo= 1
        self.rect.top = posY
        self.rect.left = posX

        self.disparoPersonaje = personaje

    #trayectoria que sigue el proyectil
    def trayectoria(self):
        if self.disparoPersonaje == "N": #Nave Espacial
            self.rect.top = self.rect.top - self.velocidadDisparo
        elif self.disparoPersonaje == "I": #Invasor
            self.rect.top = self.rect.top + self.velocidadDisparo


    def dibujar(self,superficie):
        superficie.blit(self.Img, self.rect)
