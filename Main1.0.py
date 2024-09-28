

import time
import numpy as np
import utils
def jugar():
    print(f"Welcome to Battleship")
    time.sleep(1)

    utils.dibujar_batalla_barcos()

    time.sleep(2)

    modo = ("Hay dos modos de juego: Corto( Cada jugador tendra 6 barcos de eslora 1 y quién elimine antes dos barcos habrá ganado. Largo: 6 barcos cada uno y quien elimine los del contrincante antes habrá ganado.  Introduzca: (Corto/Largo)) ")

    print(f"Creating your new the game track...")

    time.sleep(1)
    tablero_usuario = utils.crear_tablero(10)
    tablero_maquina = utils.crear_tablero(10)

    modo = ("Hay dos modos de juego: Corto( Cada jugador tendra 6 barcos de eslora 1 y quién elimine antes dos barcos habrá ganado. Largo: 6 barcos cada uno y quien elimine los del contrincante antes habrá ganado.  Introduzca: (Corto/Largo)) ")
    if modo == "corto":
        flota_usuario = utils.crear_barcos_modo_corto(tablero_usuario)
        flota_maquina = utils.crear_flota(tablero_maquina)
    else:
        flota_usuario = utils.crear_flota(tablero_usuario)
        flota_maquina = utils.crear_flota(tablero_maquina)
        #print(flota_usuario) if you want to see yours boats before placing in the game track

    time.sleep(0.5)
    print(f"Your fleet will be made up of 6 ships and they will be placed randomly on the game track.")


    tablero_final = utils.colocar_flota(flota_usuario,tablero_usuario)
    tablero_maquina_final = utils.colocar_flota(flota_maquina,tablero_maquina)
    print(f"\n               Here you are")
    print(tablero_final)

    while True: 
        respuesta = input("Te gusta tu tablero o generamos otro?(True/False)")    
        if respuesta == "True":
            print(f"Then you will play with this, GOOD LUCK!")
            break
        else:
            print("Generando nuevo tablero")
            time.sleep(1)
            tablero_final = utils.generar_nuevo_tablero()
            print(tablero_final)
        
    utils.sistema_de_turnos(tablero_final, tablero_maquina)

def hundir_la_flota():
    while True:
        jugar()
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (True/False): ").lower()
        if jugar_nuevamente != "True":
            print(f"Saliendo del juego, que tenga buen día no dude en volver a jugar")
            print(f"Con un pull de git compruebe las nuevas actualizaciones")
            break