import pygame
from pygame.locals import *
from Proyectil import Proyectil
#La clase nave espacial
#hereda a partir de la clase Sprite de pygame
class naveEspacial(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.Img = pygame.image.load("imagenes/nave.jpg")
        self.imagenExplosion = pygame.image.load("imagenes/explosion.jpg")

        #Se asigna a la imagen un rectangulo
        self.rect = self.Img.get_rect()
        self.rect.centerx = ancho / 2
        self.rect.centery= alto - 30

        self.listaDisparo = []
        self.Vida = True
        self.Velocidad = 2

        #Sonido del disparo
        self.sonidoDisparo = pygame.mixer.Sound("sonidos/disparo.wav")
        self.sonidoExplosion = pygame.mixer.Sound("sonidos/disparo.wav")


    def moverDerecha(self):
        self.rect.right += self.Velocidad
        self.__mover()

    def moverIzquierda(self):
        self.rect.left -= self.Velocidad
        self.__mover()

    #Se convierte este metodo en privado
    #en python para hacer un metodo privado
    #se pone antes del nombre dos guiones bajos
    def __mover(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 870:
                self.rect.right = 840

    def disparar(self, x, y):
        imgProyectil = "imagenes/disparoa.jpg"
        miProyectil = Proyectil(x,y,imgProyectil,"N")
        self.sonidoDisparo.play()
        self.listaDisparo.append(miProyectil)

    #Accion cuando se destruye la nave
    def destruccion(self):
        self.sonidoExplosion.play()
        self.Vida = False
        self.Velocidad = 0
        self.Img = self.imagenExplosion

    def dibujar(self,superficie):
        superficie.blit(self.Img, self.rect)
