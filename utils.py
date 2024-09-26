import numpy as np
import random
import time

def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero


def crear_barco(eslora):
    casilla_0 = (random.randint(0,9), random.randint(0,9))
    orientacion = random.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0]+1, casilla[1])
            barco.append(casilla) # Vertical
        else:
            casilla = (casilla[0], casilla[1]+1)
            barco.append(casilla) # Horizontal

    return barco


def colocar_barco_tablero(barco,tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    print(tablero)


def flota(tablero):
    lista_barcos_p =[crear_barco(2),crear_barco(2),crear_barco(2), crear_barco(3), crear_barco(3),crear_barco(4)]
    for barcos in lista_barcos_p:
        for i, j in barcos:
            if tablero[i,j] == "O":
                colocar(tablero)
            else:
                return lista_barcos_p