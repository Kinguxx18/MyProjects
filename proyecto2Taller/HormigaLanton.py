import pygame
from random import choice
from copy import deepcopy
from random import randrange
import pickle

_TAMAÑO = 5
_ANCHO = 600
_ALTO = 600

_COLUMNAS = int(_ANCHO / _TAMAÑO + 1)
_FILAS = int(_ALTO / _TAMAÑO + 1)

def main():
    """
    Programa principal de la Hormiga de Langhton
    """
    pygame.init()
    window = pygame.display.set_mode((_ANCHO, _ALTO))
    loop = True
    pausar = False
    A = limpiarM()

    hormiga = {
    "fila" : int((_ALTO / _TAMAÑO) / 2),
    "dir" : 1,
    "columnas" : int((_ANCHO / _TAMAÑO) / 2)
    }
    

    while loop:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pausar = not pausar
                if keys[pygame.K_r]:
                    hormiga["fila"] = int((_ALTO / _TAMAÑO) / 2)
                    hormiga["columnas"] = int((_ANCHO / _TAMAÑO) / 2)
                    A = limpiarM()
                if keys[pygame.K_b]:
                    hormiga["fila"] = int((_ALTO / _TAMAÑO) / 2)
                    hormiga["columnas"] = int((_ANCHO / _TAMAÑO) / 2)
                    A = limpiarM()
                if keys[pygame.K_g]:
                    archivo1 = open("saveLanton1.pkl","wb")
                    archivo2 = open("saveLanton2.pkl","wb")
                    pickle.dump(A,archivo1)
                    pickle.dump(hormiga,archivo2)
                    archivo1.close()
                    archivo2.close()
                if keys[pygame.K_c]:
                    archivo1 = open("saveLanton1.pkl","rb")
                    archivo2 = open("saveLanton2.pkl","rb")
                    A = pickle.load(archivo1)
                    hormiga = pickle.load(archivo2)
                    archivo1.close()
                    archivo2.close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                c,c2 = pygame.mouse.get_pos()
                columna = int(c / _TAMAÑO)
                fila = int(c2 / _TAMAÑO)
                A[fila][columna] = Otroestado(A[fila][columna])

        window.fill((0,0,0))
        Dibujar(A,window)
        pygame.display.update()

        if pausar ==False:
            actualizarDireccion(hormiga,A)
            Borde(hormiga)
            actualizarMatriz(A,hormiga)
            actualizarPosición(hormiga)
            
    else:
        pygame.quit()


def crearMatriz(columnas,filas,valores):
    """
    función que crea la matriz.
    Entradas. las filla y la columna.
    Restricciones: La fila y la columna debe ser válida
    Salidas:
    Generar la matriz
    """

    Matriz = []

    for a in range(filas):
        fila = []
        for b in range(columnas):
            fila.append(valores)
        Matriz. append(fila)

    return Matriz

def actualizarMatriz(A,hormiga):
    """actualiza la matriz
    """

    NuevaMatriz = deepcopy(A)

    if A[hormiga["fila"]% _FILAS][hormiga["columnas"] % _COLUMNAS] == 0:
        A[hormiga["fila"]% _FILAS][hormiga["columnas"]% _COLUMNAS] = 1
    else:
        A[hormiga["fila"]% _FILAS][hormiga["columnas"]% _COLUMNAS] = 0

    return NuevaMatriz

def MovIzquierda(direccion):
    """
   mueve la hormiga hacia la izquierda
    """
    if direccion == 3:
        return 0
    if direccion == 0:
        return 1
    if direccion == 1:
        return 2
    if direccion == 2:
        return 3

def MovDerecha(direccion):
    """
    mueve la hormiga hacía la derecha
    """
    if direccion == 1:
        return 0
    if direccion == 2:
        return 1
    if direccion == 3:
        return 2
    if direccion == 0:
        return 3




def actualizarDireccion(hormiga,A):
    """Actualiza la dirección de la hormiga
    """

    if A[hormiga["fila"]% _FILAS][hormiga["columnas"]% _COLUMNAS] == 0:
        hormiga["dir"] = MovDerecha(hormiga["dir"])
    else:
        hormiga["dir"] = MovIzquierda(hormiga["dir"])

    return hormiga

def actualizarPosición(hormiga):
    """Actualiza la posición """

    if hormiga["dir"] == 0:
        hormiga["columnas"] -= 1
        
    if hormiga["dir"] == 1:
        hormiga["fila"] += 1
        
    if hormiga["dir"] == 2:
        hormiga["columnas"] += 1

    if hormiga["dir"] == 3:
        hormiga["fila"] -=1

    
def Borde(hormiga):
    if hormiga["columnas"] > int(_ANCHO / _TAMAÑO + 1):
        hormiga["columnas"] %= int(_ANCHO / _TAMAÑO + 1)
        
    if hormiga["fila"] > int(_ANCHO / _TAMAÑO + 1):
        H["columnas"] = int(_ALTO / _TAMAÑO + 1)
        
    if hormiga["columnas"] < 0:
        hormiga["columnas"] += int(_ALTO / _TAMAÑO + 1)

    if hormiga["columnas"] < 0:
        hormiga["columnas"] += int(_ANCHO / _TAMAÑO + 1)

    return hormiga
    
def Dibujar(A,window):
    """
    función que se encarga de dubujar la hormiga
    """

    for a in range(len(A)):
        for b in range(len(A[0])):
            if A[a][b] == 1:
                color = (136 ,21 ,43)
                rec =(b * _TAMAÑO, a * _TAMAÑO, _TAMAÑO, _TAMAÑO)
                pygame.draw.rect(window,color,rec)
def limpiarM():
    """limpia  la venatana"""
    return crearMatriz(_FILAS,_COLUMNAS,0)
                

def Otroestado(estActual):
    return int((estActual + 1) % 2)


main()
