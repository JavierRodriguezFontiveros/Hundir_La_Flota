#Completo
import utils

def jugar():
    while True:
        
        print(f"Bienvenido a Hundir la flota")
        print(f"Creando tablero")

        time.sleep(1)

        tablero_usuario = utils.crear_tablero(10)
        tablero_maquina = utils.crear_tablero(10)
        print(tablero_usuario)

        time.sleep(1)
        print(f"Se va crear tu flota y la de la máquina aleatoriamente con 6 barcos")
        tablero_usuario = utils.crear_flota(tablero_usuario)
        tablero_maquina = utils.crear_flota(tablero_maquina)
        time.sleep(1)
        
        print(tablero_usuario)

        tablero_usuario = utils.colocar_flota(flota_usuario,tablero_usuario)
        tablero_usario = utils.colocar_flota(flota_maquina,tablero_maquina)

        time.sleep(1)
        print("Este es tu tablero: \n {tablero_usario}")
        print("Buena Suerte!")

        time.sleep(0.5)

        utils.sistema_de_turnos(tablero_usuario, tablero_maquina)
            
        time.sleep(1)
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (True/False): ")
        if jugar_nuevamente != "True":
            print(" # luego")
            break

jugar()
