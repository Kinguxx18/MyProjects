import pygame
#biblioteca gráfica.
from random import randrange
from copy import deepcopy
#biblioteca para guardar estados de la matriz y cargarlos.
import pickle

_ANCHO = 600
_ALTO = 600
_TAM = 5

_COLS = _ANCHO // _TAM + 1
_FILAS = _ALTO // _TAM +1

######### MATRIZ ##########
def crearMatrizRandom(filas, cols, estados):
    """
    Crea una matriz con las dimensiones indicadas y con
    valores aleatorios en el rango de [0..estados - 1].
    Entradas y Restricciones:
    -Filas.
    -Columnas.
    -Estados.
    Salidas:
    -Matriz con las dimensiones de los valores aleatorios.
    """

    M = []
    for f in range(filas):
        fila = []
        for c in range(cols):
            fila.append(randrange(estados))
        M.append(fila)
    return M

def crearMatriz(filas, cols, valor):
    """
    Crea una matriz con las dimensiones indicadas
    y con el mismo valor en todas las celdas.
    Entradas y Restricciones:
    -Filas
    -Columnas
    -Valor de las celdas
    Salidas:
    -Matriz creada.
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
    Retorna la lista con los vecinos de la celda.
    Entradas y Restricciones.
    -Matriz.
    -Fila.
    -Columna.
    Salidas:
    -Lista con los vecinos de la celda
    """
    vec = []
    for f in range(fila - 1,fila + 2):
        for c in range(col - 1, col + 2):
            if f != fila or c != col:
                vec.append(M[f % len(M)][c % len(M[0])])
    return vec

def ciclicoCrearRandom():
    """
    Crea una matriz aleatoria con cada unos de los estados.
    Entradas y restricciones:
    -Ninguna.
    Salidas:
    -Matriz Aleatoria.
    """
    return crearMatrizRandom(_FILAS,_COLS, 16)

def ciclicoCrearLimpia():
    """
    -Elimina la matriz de la pantalla de pygame.
    Entradas y restricciones:
    -Ninguna
    Salidas:
    -Pantalla de pygame vacia(en color negro).
    """
    return crearMatriz(_FILAS,_COLS, 0)

def ciclicoNext(M):
    """
    Calcula la siguiente generación de una matriz
    según las reglas del Autómata Celular Cíclico.
    Entradas y restricciones:
    -Ninguna.
    Salidas
    -Siguiente generación de la matriz.
    """
    nuevaM = deepcopy(M)
    for f in range(len(M)):
        for c in range(len(M[0])):
            vec = vecinos(M, f, c)
            NextColor = (M[f][c] + 1) % 16
            if vec.count(NextColor) >= 1:
                nuevaM[f][c] = NextColor
    return nuevaM

def ciclicoDibujar(M, window):
    """
    Se encarga de dibujar la matriz en la superficie
    window de pygame.
    Entradas y restricciones.
    -Matriz.
    -Pantalla de pygame
    Salidas:
    -Matriz dibujada en la pantalla de pygame.
    """
    for  f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 0 % 16:
                color = (255, 0, 0)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 1 % 16:
                color = (255, 165, 0)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 2 % 16:
                color = (255, 69, 0)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 3 % 16:
                color = (255, 255, 0)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 4 % 16:
                color = (144, 238, 144)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 5 % 16:
                color = (0, 255, 0)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 6 % 16:
                color = (50, 205, 50)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 7 % 16:
                color = (0, 255, 127)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 8 % 16:
                color = (72, 209, 204)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 9 % 16:
                color = (135, 206, 250)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 10 % 16:
                color = (0, 0, 255)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 11 % 16:
                color = (0, 0, 139)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 12 % 16:
                color = (128, 0, 128)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 13 % 16:
                color = (255, 0, 255)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 14 % 16:
                color = (255, 20, 147)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            if M[f][c] == 15 % 16:
                color = (220, 20, 60)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window, color, rec)
            

def ciclicoSiguiente(estado):
    """
    Realiza el cambio de estado de las celulas en la matriz.
    Entradas y restricciones:
    -Estado en el que se encuentra la celula en la matriz
    Salida:
    -Cambio de estado de la celula
    """
    return (estado + 1) % 16

def ciclico():
    """
    Subrutina que invoca las funciones para retornar como resultado
    el Autómata Celular Cíclico.
    Entradas y Restricciones:
    Ningunas
    Salidas:
    -Autómata Celular Cíclico.
    """
    pygame.init()
    window = pygame.display.set_mode((_ANCHO, _ALTO))
    loop = True
    pause = False
    M = ciclicoCrearRandom() 
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
                    M = ciclicoCrearRandom()
                if keys[pygame.K_b]:
                    M = ciclicoCrearLimpia()
                if keys[pygame.K_g]:
                    archivo = open("saveCiclico.pkl" , "wb")
                    pickle.dump(M,archivo)
                    archivo.close()
                if keys[pygame.K_c]:
                    archivo = open("saveCiclico.pkl" , "rb")
                    M = pickle.load(archivo)
                    archivo.close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                c = x // _TAM
                f = y // _TAM
                M[f][c] = ciclicoSiguiente(M[f][c])
                
        window.fill((0, 0, 0))
        ciclicoDibujar(M, window)
        pygame.display.update()
        if not pause:
            M = ciclicoNext(M)
            
    pygame.quit()
    
ciclico()
