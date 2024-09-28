import numpy as np
import random
import time

def dibujar_batalla_barcos():
    escena = [
        "      __|__                     __|__      ",
        "     |o o o|                   |o o o|     ",
        "  ___/_____/\\__             ___/_____/\\__   ",
        "  \\           /             \\           /   ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "               #-------->>                    ",
        "                BOOOOOM!                      ",]
    for linea in escena:
        print(linea)


def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero


def crear_barco(eslora, tablero):
    while True:
        casilla_0 = (random.randint(0, 9), random.randint(0, 9))
        orientacion = random.choice(["Vertical", "Horizontal"])

        barco = [casilla_0]
        casilla = casilla_0

        for _ in range(1, eslora): #_sifnifica que se va iterar tantas veces se necesite, es una convencion de python
            if orientacion == "Vertical":
                nueva_casilla = (casilla[0] + 1, casilla[1])
            else:
                nueva_casilla = (casilla[0], casilla[1] + 1)

            if nueva_casilla[0] > 9 or nueva_casilla[1] > 9:
                break  
            barco.append(nueva_casilla)
            casilla = nueva_casilla

        if len(barco) == eslora: 
            if not comprobar_colision(barco, tablero):
                return barco
        
def crear_barco_modo_corto(tablero)
    barcos=[]
    for _ in range(6):
        barco = [(random.randint(0, 9), random.randint(0, 9))]
        while comprobar_colision(barco, tablero):
            barco = [(random.randint(0, 9), random.randint(0, 9))]
        barcos.append(barco)
        colocar_flota([barco], tablero)
    return barcos

def comprobar_colision(barco, tablero): 
    for i, j in barco:
        if tablero[i][j] == 'O':  
            return True
    return False

def crear_flota(tablero):
    flota_barcos = [
        crear_barco(2, tablero),
        crear_barco(2, tablero),
        crear_barco(2, tablero),
        crear_barco(3, tablero),
        crear_barco(3, tablero),
        crear_barco(4, tablero)]
    return flota_barcos

def colocar_flota(flota, tablero): 
    for barco in flota:
        for i, j in barco:
            tablero[i][j] = 'O'  
    return tablero

def generar_nuevo_tablero():
    tablero_usuario = crear_tablero(10)
    flota_usuario = crear_flota(tablero_usuario)
    tablero_final = colocar_flota(flota_usuario, tablero_usuario)
    return tablero_final

#Hasta aquí funciones para preparar el juego
#Apartir de aqui empieza el sistema de turnos

def sistema_de_turnos(tablero_final, tablero_maquina):
    print("Que comience el juego")
    puntos_usuario = 0
    puntos_maquina = 0
    if modo == "corto":
        limite_puntos = 2
    else:
        limite_puntos = len(tablero_final[tablero_final == "O"])
    
    while puntos_usuario < limite_puntos and puntos_maquina < limite_puntos:
        print("\n--- Tu turno ---")    
        puntos_usuario += turno_usuario(tablero_maquina)
        
        if puntos_usuario > limite_puntos:   
            print("Has ganado makena.")
            break
        time.sleep(1)

        print("\n--- Turno de la Máquina ---")   
        puntos_maquina += turno_maquina(tablero_final)
        print(tablero_final)

        if puntos_maquina >= limite_puntos:      
            print("La máquina te ha ganado crack")
            break

def verificar_victoria(tablero_oponente,modo):
    if modo == "Corto":
        barcos_restantes = len(np.where(tablero_oponente == "O")[0])
        barcos_hundidos = 6 - barcos_restantes
        return barcos_hundidos >= 2 #Gana si almenos se hunden dos barcos
    else:
        return not np.any(tablero_oponente == "O") #Gana si no queda ningun barco

def turno_usuario(tablero):
    while True:  
        try:                                                                 #Mientras no se pierda el turno
            fila = int(input("Introduce la fila (1-9) a la que quieres disparar: "))
            columna = int(input("Introduce la columna (1-9) a la que quieres disparar: "))
            if not (0 <= fila <= 9) or not columna (0 <= columna <= 9):
                print("Cordenadas fuera de rango, intentelo de nuevo")
                continue
        except ValueError:
            print("Intruce numero entre el 1 y 9.")
            continue

        resultado = disparar((fila-1, columna-1), tablero)             #llamada ala función disparar
        print(f"Disparaste a {(fila, columna)}:\n {resultado}")     #Ubicación del tiro por pantalla
        
        if resultado == "Agua":                                     #Posibilidades
            print("Fallaste. Fin de tu turno.")
            return 0
        elif resultado == "Tocado":
            print("Has acertado sigue disparando.")
            if barco_hundido(tablero):
                print("Barco Hundido")
                return 1
            

def turno_maquina(tablero):
    while True:                      #Mientras acierte seguirá disparando de forma random
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        
        resultado = disparar((fila, columna), tablero)
        print(f"La máquina disparó a {(fila, columna)}: \n {resultado}")
        
        if resultado == "Agua":
            print("La máquina falló. Fin de su turno.")
            return 0  

        elif resultado == "Tocado":
            print("La máquina acertó. Sigue disparando.")
            return 1
        

def disparar(casilla, tablero):
    fila, columna = casilla
    if tablero[fila, columna] == "O":              #la O es barco, la X tocado y la A agua
        print("Tocado")
        tablero[fila, columna] = "X"
        return "Tocado"
    elif tablero[fila,columna] == '_': 
        print("Agua")
        tablero[fila,columna] = "A"
        return "Agua"
    else:
        print("Casilla ya disparada.")
        return "Casilla repetida"
    

def barco_hundido(tablero,fila,columna):
    return not np.any(tablero == "O")

def crear_barcos_modo_corto(tablero):
    barcos = []
    for _ in range(6):
        barco = crear_barco(1, tablero)  
        barcos.append(barco)
    return barcos
