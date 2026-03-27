import pygame
from random import choice 
from copy import deepcopy
import pickle

_ANCHO = 800
_ALTO = 600
_TAM = 5

_COLS = _ANCHO // _TAM + 1
_FILAS = _ALTO // _TAM +1

def crearMatrizRandom(filas, cols, estados):
    """
    Crea una matriz con las dimensiones indicadas y con
    valores aleatorios en el rango de [0..estados - 1].
    """

    M = []
    for f in range(filas):
        fila = []
        for c in range(cols):
            fila.append(choice([0,1,2]))
        M.append(fila)
    return M

def crearMatriz(filas, cols, valor):
    """
    crea una matriz con las dimensiones indicadas
    y con el mismo valor en todas las celdas.
    """
    M = []
    for f in range(filas):
        fila = []
        for c in range(cols):
            fila.append(valor)
        M.append(fila)
    return M

def vecinos(M, fila, col):
    """
    Retorna la lista con los vecinos de la celda
    """
    vec = []
    for f in range(fila - 1,fila + 2):
        for c in range(col - 1, col +2):
            if f != fila or c != col:
                vec.append(M[f % len(M)][c % len(M[0])])
    return vec

def bryansCrearRandom():
    return crearMatrizRandom(_FILAS,_COLS, 2)

def bryansCrearLimpia():
    return crearMatriz(_FILAS,_COLS, 0)

def bryansNext(M):
    """
    Calcula la siguiente generación de una matriz
    según las reglas del Autómata de Bryans Brian.
    """
    nuevaM = deepcopy(M)
    for f in range(len(M)):
        for c in range(len(M[0])):
            vec = vecinos(M, f, c)
            if M[f][c] == 0 and vec.count(2) == 2:
                nuevaM[f][c] = 2
            elif M[f][c] == 2:
                nuevaM[f][c] = 1
            elif M[f][c] == 1:
                nuevaM[f][c] = 0
    return nuevaM

def bryansDibujar(M, window):
    """
    Se encarga de dibujar la matriz en la superficie
    window de pygame.
    """
    for  f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 2:
                color = (0,40,255)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            elif M[f][c] == 1:
                color = (0,100,240)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            
def bryansSiguiente(estado):
    return (estado + 1) % 3

def bryans():
    """
    Subrutina que invoca las funciones para retornar como resultado
    el Juego de La Vida de Conway
    Entradas y Restricciones:
    Ningunas
    Salidas:
    -Juego de la Vida.
    """
    pygame.init()
    window = pygame.display.set_mode((_ANCHO, _ALTO))
    loop = True
    pause = False
    M = bryansCrearRandom() 
    while loop:
        pygame.time.delay(16)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pause = not pause
                if keys[pygame.K_r]:
                    M = bryansCrearRandom()
                if keys[pygame.K_b]:
                    M = bryansCrearLimpia()
                if keys[pygame.K_g]:
                    archivo = open("saveBryans.pkl","wb")
                    pickle.dump(M,archivo)
                    archivo.close()
                if keys[pygame.K_c]:
                    archivo = open("saveBryans.pkl","rb")
                    M = pickle.load(M,archivo)
                    archivo.close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                c = x // _TAM
                f = y // _TAM
                M[f][c] = bryansSiguiente(M[f][c])
                
        window.fill((0, 0, 0))
        bryansDibujar(M, window)
        pygame.display.update()
        if not pause:
            M = bryansNext(M)
    pygame.quit()
    
bryans()
