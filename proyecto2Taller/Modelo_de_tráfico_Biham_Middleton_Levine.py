import pygame
#biblioteca gráfica.
from random import choice, randrange
from copy import deepcopy
#Biblioteca para cargar y guardar estados.
import pickle

_ANCHO = 600
_ALTO = 500
_TAM = 2

_COLS = _ANCHO // _TAM + 1
_FILAS = _ALTO // _TAM +1

######### MATRIZ ##########

def createrMatrizRandom(filas, cols, estados):
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
            fila.append(choice([0,0,0,1,2]))
        M.append(fila)
    return M

def createrMatriz(filas, cols, valor):
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

def traficCreaterRandom():
    """
    Crea una matriz aleatoria con cada unos de los estados.
    Entradas y restricciones:
    -Ninguna.
    Salidas:
    -Matriz Aleatoria.
    """
    return createrMatrizRandom(_FILAS,_COLS, 3)

def traficCreaterDelated():
    """
    -Elimina la matriz de la pantalla de pygame.
    Entradas y restricciones:
    -Ninguna
    Salidas:
    -Pantalla de pygame vacia(en color negro).
    """
    return createrMatriz(_FILAS,_COLS, 0)

######## CARS ############

def traficCarsRed(M):
    """
    Calcula la siguiente generación de una matriz
    según las reglas del Modelo de tráfico Biham-Middleton-Levine.
    Entradas y restricciones:
    -Ninguna.
    Salidas
    -Siguiente generación de la matriz.
    """
    M2 = deepcopy(M)
    for f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 2:
                if M[f][(c + 1) % _COLS] == 0:
                    M[f][c]= 0
                    M[f][(c + 1) % _COLS] = 2

    return M
def traficCarsBlue(M):
    """
    Se encarga de dibujar la matriz en la superficie
    window de pygame para "los carros de color azul".
    Entradas y restricciones.
    -Matriz.
    -Pantalla de pygame
    Salidas:
    -Matriz dibujada en la pantalla de pygame.
    """
    M2 = deepcopy(M)
    for  f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 1:
                if M2[(f + 1)% _FILAS][c] == 0:
                    M2[f][c] = 0
                    M2[(f + 1)% _FILAS][c]= 1
    return M2
    
def traficDrawCars(M, window):
    """
    Se encarga de dibujar la matriz en la superficie
    window de pygame para "los carros de color rojo".
    Entradas y restricciones.
    -Matriz.
    -Pantalla de pygame
    Salidas:
    -Matriz dibujada en la pantalla de pygame.
    """
    for  f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 2:
                color = (253, 21, 50)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window,color,rec)
            if M[f][c] == 1:
                color = (41, 208, 253)
                rec = (c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window,color,rec)

def traficNextStade(estado):
    """
    Realiza el cambio de estado de las celulas en la matriz.
    Entradas y restricciones:
    -Estado en el que se encuentra la celula en la matriz
    Salida:
    -Cambio de estado de la celula
    """
    return (estado + 1) % 3
########## PRINCIPAL #########
def trafic():
    """
    Subrutina Principal que invoca las funciones para retornar como resultado
    el Modelo de tráfico Biham-Middleton-Levine .
    Entradas y Restricciones:
    Ningunas
    Salidas:
    -Modelo de tráfico Biham-Middleton-Levine.
    """
    pygame.init()
    window = pygame.display.set_mode((_ANCHO, _ALTO))
    loop = True
    pause = False
    M = traficCreaterRandom() 
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
                    M = traficCreaterRandom()
                if keys[pygame.K_b]:
                    M = traficCreaterDelated()
                if keys[pygame.K_g]:
                    archivo = open("saveTrafic.pkl" , "wb")
                    pickle.dump(M,archivo)
                    archivo.close()
                if keys[pygame.K_c]:
                    archivo = open("saveTrafic.pkl" , "rb")
                    M = pickle.load(archivo)
                    archivo.close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                c = x // _TAM
                f = y // _TAM
                M[f][c] = traficNextStade(M[f][c])
                
        window.fill((255, 255, 255))
        if not pause:
            M2 = traficCarsBlue(M)
            M = traficCarsRed(M2)
        traficDrawCars(M, window)
        pygame.display.update()
    pygame.quit()


trafic()
