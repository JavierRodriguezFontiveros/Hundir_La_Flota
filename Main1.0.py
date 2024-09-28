import time
import numpy as np
import utils

def jugar():
    print(f"Welcome to Battleship")
    time.sleep(1)

    utils.dibujar_batalla_barcos()

    time.sleep(2)

    modo = input("Hay dos modos de juego: Corto( Cada jugador tendra 6 barcos de eslora 1 y quién elimine\
                 \ antes dos barcos habrá ganado. Largo: 6 barcos cada uno y quien elimine los del\
                  contrincante antes habrá ganado.  Introduzca: (Corto/Largo)) ").lower()

    print(f"Creating your new the game track...")

    time.sleep(1)
    tablero_usuario = utils.crear_tablero(10)
    tablero_maquina = utils.crear_tablero(10)

    
    if modo == "corto":
        flota_usuario = [utils.crear_barcos(1,tablero_usuario) for _ in range(6)]
        flota_maquina = [utils.crear_barcos(1,tablero_maquina) for _ in range(6)]
    else:
        flota_usuario = utils.crear_flota(tablero_usuario)
        flota_maquina = utils.crear_flota(tablero_maquina)
        
    time.sleep(0.5)
    print(f"Your fleet will be made up of 6 ships and they will be placed randomly on the game track.")
    print(tablero_usuario)

    while True: 
        respuesta = input("Te gusta tu tablero o generamos otro?(si/no)").lower()    
        if respuesta == "si":
            print(f"Then you will play with this, GOOD LUCK!")
            break
        else:
            tablero_usuario = utils.crear_tablero(10)
            flota_usuario = utils.crear_flota(tablero_usuario)
            utils.colocar_flota(flota_usuario,tablero_usuario)
            print("Nuevo tablero")
            print(tablero_usuario)


            
        
    utils.sistema_de_turnos(tablero_usuario, tablero_maquina, flota_usuario, flota_maquina, modo)

def hundir_la_flota():
    while True:
        jugar()
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_nuevamente != "si":
            print(f"Saliendo del juego, que tenga buen día no dude en volver a jugar")
            print(f"Con un pull de git compruebe las nuevas actualizaciones")
            break

hundir_la_flota()