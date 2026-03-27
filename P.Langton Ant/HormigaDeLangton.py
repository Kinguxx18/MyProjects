import pygame
from random import randrange,choice
from copy import deepcopy

#______________________________________________________________________________________________________________________________________

#Hormiga del Langton
#Jeramy Mairena 2022

_ANCHO = 900
_ALTO = 500
_TAM = 5

_COLUM = _ANCHO // _TAM + 1
_FILAS = _ALTO // _TAM + 1

def crearMatrizLangton(filas,colum,valor):
    """
    Crea una matriz con el tamaño indicad0 y con el mismo valor en
    todas las celdas.
    Entradas y restricciones:
    - filas: fila de la matriz válida
    - colum: columna de la matriz válida
    - valor: número a insertar en todas las filas y columnas de la matriz
    Salidas:
    - Matriz en blanco
    """

    H = []

    for f in range(filas):
        fila = []
        for c in range(colum):
            fila.append(valor)
        H. append(fila)

    return H 

def matrizLimpiaLangton():
    """funcion que limpia la ventana de Pygame"""
    return crearMatrizLangton(_FILAS,_COLUM,0)

def updateMatrizLangton(M,H):
    """funcion que actualiza los elementos en ventana"""

    nuevaM = deepcopy(M)

    if M[H["fila"]% _FILAS][H["colum"] % _COLUM] == 0:
        M[H["fila"]% _FILAS][H["colum"]% _COLUM] = 1
    else:
        M[H["fila"]% _FILAS][H["colum"]% _COLUM] = 0

    return nuevaM

def updateDirecHormiga(H,M):
    """función que actualiza la direccion de la hormiga
    entradas y restricciones:
    H:Lugar de la hormiga
    M: La direccion hacia la que se mueve la hormiga
    salidas:
    la posicion de la hormiga actualizada"""

    if M[H["fila"]% _FILAS][H["colum"]% _COLUM] == 0:
        H["direc"] = direcRIGHT(H["direc"])
    else:
        H["direc"] = direcLEFT(H["direc"])

    return H

def updatePosHormiga(H):
    """función que actualiza la posicion de la hormiga
    entradas y restricciones:
    H:Lugar de la hormiga 
    salidas:
    la posicion de la hormiga actualizada"""

    if H["direc"] == 0:
        H["colum"] -= 1
        
    if H["direc"] == 1:
        H["fila"] += 1
        
    if H["direc"] == 2:
        H["colum"] += 1

    if H["direc"] == 3:
        H["fila"] -=1

def direcLEFT(sentido):
    """
    Cambia la dirección cunando la hormiga va hacia la izquiera
    Entradas y restricciones:
    - sentido: direccion de la hormiga
    Salidas:
    - Cambio de direccion
    """

    if sentido == 0:
        return 1
    elif sentido == 1:
        return 2
    elif sentido == 2:
        return 3
    elif sentido == 3:
        return 0

def direcRIGHT(sentido):
    """
    Cambia la dirección cunando la hormiga va hacia la derecha 
    Entradas y restricciones:
    - sentido: direccion de la hormiga
    Salidas:
    - Cambio de direccion
    """

    if sentido == 0:
        return 3
    elif sentido == 3:
        return 2
    elif sentido == 2:
        return 1
    elif sentido == 1:
        return 0
    
def boardLangton(H):
    if H["colum"] > _ANCHO // _TAM + 1:
        H["colum"] %= _ANCHO // _TAM + 1
        
    if H["colum"] < 0:
        H["colum"] += _ANCHO // _TAM + 1

    if H["fila"] > _ANCHO // _TAM + 1:
        H["colum"] = _ALTO // _TAM + 1
        
    if H["colum"] < 0:
        H["colum"] += _ALTO // _TAM + 1

    return H
    
def DibujarLangton(M,window):
    """
    Se encarga de dibujar la matriz en pantalla
    Entradas y restricciones:
    - Matriz: matriz válida
    - Window: superficie de pygame
    Salidas:
    - Dibujo del autómata en pantalla
    """

    for f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 1:
                color = (255 ,255 ,255)
                rec =(c * _TAM, f * _TAM, _TAM, _TAM)
                pygame.draw.rect(window,color,rec)
                

def siguienteEstadoHormiga(estado):
    return (estado + 1) % 2

def mainHormigaDeLangton():
    """
    Función que recibe las ordenes de las demas funciones
    para lograr el correcto uso del automata
    """
    pygame.init()
    window = pygame.display.set_mode((_ANCHO, _ALTO))
    loop = True
    pause = False
    M = matrizLimpiaLangton()

    H = {
    "fila" : (_ALTO // _TAM) // 2,
    "colum" : (_ANCHO // _TAM) // 2,
    "direc" : 1
    }
    

    while loop:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pause = not pause
                if keys[pygame.K_r]:
                    H["fila"] = (_ALTO // _TAM) // 2
                    H["colum"] = (_ANCHO // _TAM) // 2
                    M = matrizLimpiaLangton()
                if keys[pygame.K_b]:
                    H["fila"] = (_ALTO // _TAM) // 2
                    H["colum"] = (_ANCHO // _TAM) // 2
                    M = matrizLimpiaLangton()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                c = x // _TAM
                f = y // _TAM
                M[f][c] = siguienteEstadoHormiga(M[f][c])

        window.fill((0,0,0))
        
        DibujarLangton(M,window)
        pygame.display.update()

        if not pause:
            updateDirecHormiga(H,M)
            boardLangton(H)
            updateMatrizLangton(M,H)
            updatePosHormiga(H)
            
    try:
        pygame.quit()
    except:
        print("El programa ha finalizado")
        
mainHormigaDeLangton()
