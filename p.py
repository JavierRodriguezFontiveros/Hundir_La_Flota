import utils
import time

print(f"Bienvenido a Hundir la Flota")
time.sleep(1)
utils.dibujar_batalla_barcos()
time.sleep(2)

while True:
    modo = input("Hay dos modos de juego: Corto (6 barcos de eslora 1) o Largo (6 barcos de diferentes esloras). Introduzca (Corto/Largo): ").lower()
    if modo == "corto" or modo == "largo":
        break
    else:
        print("Modo no válido. Por favor, introduzca 'Corto' o 'Largo'.")

print(f"Creando tablero de juego...")
time.sleep(1)

#Crear tableros
tablero_usuario = utils.crear_tablero(10)
tablero_maquina = utils.crear_tablero(10)

#Crear flotas
if modo == "corto":
    flota_usuario = utils.crear_flota(tablero_usuario, [1] *6)
    flota_maquina = utils.crear_flota(tablero_maquina, [1] *6)
elif modo == "largo":
    flota_usuario = utils.crear_flota(tablero_usuario, [2,2,2,3,3,4])
    flota_maquina = utils.crear_flota(tablero_maquina, [2,2,2,3,3,4])

#Colocar flotas
utils.colocar_flota(flota_usuario,tablero_usuario)
utils.colocar_flota(flota_maquina,tablero_maquina)

time.sleep(0.5)
print(f"\n   Tu tablero")
utils.mostrar_tablero(tablero_usuario)

while True: 
    respuesta = input("Te gusta tu tablero o generamos otro?(si/no)").lower()    
    if respuesta == "si":
        print(f"Entonces jugarás con este, ¡BUENA SUERTEE!")
        break
    else:
        time.sleep(0.5)
        tablero_usuario = utils.crear_tablero(10)
        if modo == "corto":
            flota_usuario = utils.crear_flota(tablero_usuario, [1] * (6))
        else:
            flota_usuario = utils.crear_flota(tablero_usuario, [2, 2, 2, 3, 3, 4])
        utils.colocar_flota(flota_usuario,tablero_usuario)  
        print("Nuevo tablero Generado")  
        utils.mostrar_tablero(tablero_usuario)

utils.sistema_de_turnos(tablero_usuario, tablero_maquina, flota_usuario, flota_maquina, modo)


