import pygame
import sys
from pygame.locals import *
from clases import naveEspacial
from clases import Invasor

#variables globales
ancho = 900
alto = 480
listaEnemigo = []

def terminarJuego():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)

        enemigo.conquista = True


def CargarEnemigos():
    posX = 100
    for x in range(1,5):
        enemigo1 = Invasor(posX,100,40, 'imagenes/marcianoA.jpg', 'imagenes/marcianoB.jpg')
        listaEnemigo.append(enemigo1)
        posX = posX + 200

    posX = 100
    for x in range(1,5):
        enemigo1 = Invasor(posX,0,40, 'imagenes/marciano2A.jpg', 'imagenes/marciano2B.jpg')
        listaEnemigo.append(enemigo1)
        posX = posX + 200

    posX = 100
    for x in range(1,5):
        enemigo1 = Invasor(posX,-100,40, 'imagenes/marciano3A.jpg', 'imagenes/marciano3B.jpg')
        listaEnemigo.append(enemigo1)
        posX = posX + 200


def Main():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Space Invaders")
    ImagenFondo = pygame.image.load("imagenes/Fondo.jpg")

    ##Musica de Fondo
    pygame.mixer.music.load("sonidos/intro.mp3")
    #el numero indica el numero de veces que se va repetir el sonido
    pygame.mixer.music.play(3)

    miFuente = pygame.font.Font("fonts/Sketch3D.otf", 60)
    color = (255,195,0)
    miTexto = miFuente.render("GAME OVER",0,color)


    enJuego = True
    jugador = naveEspacial(ancho,alto)

    CargarEnemigos()
    reloj = pygame.time.Clock()
    #Se crea el proyectil centrado, cercado a la nave
    #DemoProyectil = Proyectil(ancho/2,alto-30)
    while True:

        #Tiempo para regular los frames
        #A mas tiempo mas velocidad del juego
        reloj.tick(50)
        tiempo = pygame.time.get_ticks()/1000

        #jugador.mover()
        #DemoProyectil.trayectoria()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

        if (enJuego == True):
            if evento.type == pygame.KEYDOWN:
                if evento.key ==K_LEFT:
                    jugador.moverIzquierda()
                elif evento.key == K_RIGHT:
                    jugador.moverDerecha()
                elif evento.key == K_LCTRL:
                    x,y = jugador.rect.center
                    #print (" x = " + str(x), " y = ", str(y))
                    jugador.disparar(x,y)

        ventana.blit(ImagenFondo, (0,0))
        #enemigo.comportamiento(tiempo)
        jugador.dibujar(ventana)
        #enemigo.dibujar(ventana)

        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
            if x.rect.top < 10:
                jugador.listaDisparo.remove(x)
            else:
                for enemigo in listaEnemigo:
                    #Si algun disparo colisiona con un enemigo
                    if x.rect.colliderect(enemigo.rect):
                        listaEnemigo.remove(enemigo) #elimina enemigo
                        jugador.listaDisparo.remove(x) #elimina disparo

        if len(listaEnemigo) > 0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                #Si el enemigo colisiona con nuestra nave
                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego = False
                    terminarJuego()


                if len(enemigo.listaDisparo) > 0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        #Si el disparo enemigo colisiona con la nave
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego == False
                            terminarJuego()

                    if x.rect.top > 900:
                        enemigo.listaDisparo.remove(x)
                    else:
                        for disparo in jugador.listaDisparo:
                            #Si algun disparo colisiona con un disparo enemigo
                            if x.rect.colliderect(disparo.rect):
                                jugador.listaDisparo.remove(disparo) #elimina disparo
                                enemigo.listaDisparo.remove(x) #elimina disparo enemigo

        if enJuego == False:
            #La musica se ira deteniendo poco a poco
            ventana.blit(miTexto,(300,300))
            pygame.mixer.music.fadeout(3000)


        pygame.display.update()

Main()