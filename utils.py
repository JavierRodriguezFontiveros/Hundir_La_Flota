import numpy as np
import random
import time


def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero
tablero_copy =crear_tablero(10)

#Actualizacion
def tablero_final (crear_barco,crear_flota,colocar_flota)
    crear_barco()
    crear_barco()
    colocar_flota()
    return tablero_final

def crear_barco(eslora):
    casilla_0 = (random.randint(0,9), random.randint(0,9))  #2 posiciones aleatorias
    orientacion = random.choice(["Vertical", "Horizontal"])  #posicion aleatoria

    barco = [casilla_0] #Los barcos seran listas
    casilla = casilla_0

    while len(barco) < eslora:               #Código para hacerlo crecer en la longitud y posicion que le toque
        if orientacion == "Vertical":
            casilla = (casilla[0]+1, casilla[1])
            barco.append(casilla) # Vertical          #Suma valor al barco
        else:
            casilla = (casilla[0], casilla[1]+1)
            barco.append(casilla) # Horizontal
    
    for x,y in barco:
        if x == len(tablero_copy) or y == len(tablero_copy):
            return crear_barco(eslora)

    return barco                             #cada barco será una lista de tuplas

def comprobar_colision(barco, tablero): #FUNCIONA PERFECTAMENTE
    for i, j in barco:
        if tablero[i][j] == 'O':  
            return True
    return False

def colocar_flota(flota, tablero): #FUNCIONA PERFECTAMENTE
    flota_barcos = [
        crear_barco(2, tablero),
        crear_barco(2, tablero),
        crear_barco(2, tablero),
        crear_barco(3, tablero),
        crear_barco(3, tablero),
        crear_barco(4, tablero)]
    for barco in flota_barcos:
        for i, j in barco:
            tablero[i][j] = 'O'  
    return tablero






def disparar(casilla, tablero):
    if tablero[casilla] == "O":              #la O es barco, la X tocado y la A agua
        print("Tocado")
        tablero[casilla] = "X"
    elif tablero[casilla] == '_': 
        print("Agua")
        tablero[casilla] = "A"
    return tablero







def crear_flota(tablero):
    flota_barcos =[crear_barco(2),crear_barco(2),crear_barco(2), crear_barco(3), crear_barco(3),crear_barco(4)]
    for barcos in flota_barcos:
        for i, j in barcos:
            if tablero[i,j] == "O":
                crear_flota(tablero)
            else:
                return flota_barcos

#Crear una lista de barcos, de uno en uno ira comprobando que donde estén colocados no haya otro barco,
#Tenemos una recursividad




def turno_usuario(tablero):
    while True:                                                                   #Mientras no se pierda el turno
        fila = int(input("Introduce la fila (0-9) a la que quieres disparar: "))
        columna = int(input("Introduce la columna (0-9) a la que quieres disparar: "))

        resultado = disparar((fila, columna), tablero)             #llamada ala función disparar
        print(f"Disparaste a {(fila, columna)}:\n {resultado}")     #Ubicación del tiro por pantalla
        
        if resultado == "Agua":                                     #Posibilidades
            print("Fallaste. Fin de tu turno.")
            break
        elif resultado == "Tocado":
            print("Has acertado sigue disparando.")
            continue
        else:
            print("Casilla repetida,perdiste el turno")
            break








def turno_maquina(tablero):
    while True:                      #Mientras acierte seguirá disparando de forma random
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        
        resultado = disparar((fila, columna), tablero)
        print(f"La máquina disparó a {(fila, columna)}: \n {resultado}")
        
        if resultado == "Agua":
            print("La máquina falló. Fin de su turno.")
            break  

        elif resultado == "Tocado":
            print("La máquina acertó. Sigue disparando.")
            continue 
        
        else:
            print("Casilla repetida, pierde el turno")
            break




def verificar_victoria(tablero_oponente):
    return not np.any(tablero_oponente == "O")

#Si quedan alguna "O" nos dá True, nadie ha ganado




def sistema_de_turnos(tablero_usuario, tablero_maquina):
    print("Que comience el juego")
    
    while verificar_victoria(tablero_maquina) and verificar_victoria(tablero_usuario): #Mientras ninguno haya ganado..
        print("\n--- Tu turno ---")    
        turno_usuario(tablero_maquina)
        
        if not verificar_victoria(tablero_maquina):   #Verifica si gana
            print("Has ganado makena.")
            break
        
        print("\n--- Turno de la Máquina ---")   
        turno_maquina(tablero_usuario)

        if not verificar_victoria(tablero_usuario):      
            print("La máquina te ha ganado crack")
            break