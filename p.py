
#Import de bibliotecas necesarias:
import time
import random
import numpy as np
import utils

print(f"Welcome to Battleship")
time.sleep(1)
print(f"Creating your new the game track...")

time.sleep(1)
print(f"\n               Here you are")
tablero_usuario = utils.crear_tablero(10)
tablero_maquina = utils.crear_tablero(10)
print(tablero_usuario)

time.sleep(1)
print(f"Your fleet will be made up of 6 ships and they will be placed randomly on the game track.")

flota_usuario = utils.crear_flota(tablero_usuario)
print(flota_usuario) #if you want to see yours boats before placing in the game track

tablero_final(tablero_usuario)

while True: #Dberia poner otra definicion
    respuesta = intput("Te gusta tu tablero o generamos otro?(True/False)")    
    if respuesta == "True":
        print(f"Nice")
        break
    else:
        print("Generando nuevo tablero")
        time.sleep(1)
        tablero_final(,,)
        print(tablero_final)
        continue

#time.sleep(1)
#tablero_usuario = utils.colocar_flota(flota_usuario,tablero_usuario)
#print(tablero_usuario)
