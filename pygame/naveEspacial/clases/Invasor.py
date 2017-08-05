import pygame
from pygame.locals import *
from Proyectil import Proyectil
from random import randint

#La clase Invasor
#hereda a partir de la clase Sprite de pygame
class Invasor(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, posX, posY, distancia, imagenUno, imagenDos):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load(imagenUno)
        self.imagenB = pygame.image.load(imagenDos)

        self.listaImagenes = [self.imagenA, self.imagenB]
        self.posImagen = 0

        self.imagenInvasor = self.listaImagenes[self.posImagen]


        #Se asigna a la imagen un rectangulo
        self.rect = self.imagenInvasor.get_rect()
        #self.rect.centerx = 900 / 2
        #self.rect.centery= 480 - 30

        self.listaDisparo = []
        self.Velocidad = 20
        self.rect.top = posY
        self.rect.left = posX

        self.tiempoCambio = 1
        self.rangoDisparo = 5

        #atributos que permiten controlar el movimiento del invasor
        self.derecha = True
        self.contador = 0
        self.maxDescenso = self.rect.top + 40

        self.limiteDerecha = posX + distancia
        self.limiteIzquierda = posX - distancia
        #esta bandera se emplea para saber si termino el juego
        self.conquista = False

    #Este metodo controla la animacion
    #del Invasor
    def comportamiento(self, tiempo):
        if self.conquista == False:
            self.__movimientos()
            self.__atacar()

            if self.tiempoCambio == tiempo:
                self.posImagen += 1
                self.tiempoCambio +=1

                if self.posImagen > len(self.listaImagenes) - 1:
                    self.posImagen = 0


    def dibujar(self,superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        #superficie.blit(self.Img, self.rect)
        superficie.blit(self.imagenInvasor, self.rect)

    def __movimientos(self):
        if self.contador < 3:
            self.__movimientoLateral()
        else:
            self.__descender()


    def __descender(self):
        if self.maxDescenso == self.rect.top:
            self.contador = 0
            self.maxDescenso = self.rect.top + 40
        else:
            self.rect.top += 1

    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left + self.Velocidad
            if self.rect.left > self.limiteDerecha:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left = self.rect.left - self.Velocidad
            if self.rect.left < self.limiteIzquierda:
                self.derecha = True


    def __atacar(self):
        if (randint(0,100) < self.rangoDisparo):
            self.__disparar()

    def __disparar(self):
        x,y = self.rect.center
        imgProyectil = "imagenes/disparob.jpg"
        miProyectil = Proyectil(x,y,imgProyectil,"I")
        self.listaDisparo.append(miProyectil)
