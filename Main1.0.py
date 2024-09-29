import utils
import time
def interfaz_del_juego():

    utils.seleccionar_idioma()

    print(utils.traducciones[idioma]["bienvenida"])
    time.sleep(1)
    utils.dibujar_batalla_barcos()
    time.sleep(2)

    while True:
        modo = input(traducciones[idioma]["elige_modo"]).lower()
        if modo == "corto" or modo == "largo":
            break
        else:
            print(traducciones[idioma]["modo_no_valido"])

    print(traducciones[idioma]["creando_tablero"])
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
        respuesta = input(traducciones[idioma]["te_gusta_el_tablero"]).lower()    
        if respuesta == "si":
            print(traducciones[idioma]["jugaras_con_este"])
            break
        else:
            time.sleep(0.5)
            tablero_usuario = utils.crear_tablero(10)
            if modo == "corto":
                flota_usuario = utils.crear_flota(tablero_usuario, [1] * (6))
            else:
                flota_usuario = utils.crear_flota(tablero_usuario, [2, 2, 2, 3, 3, 4])
            utils.colocar_flota(flota_usuario,tablero_usuario)  
            print(traducciones[idioma]["nuevo_tablero_generado"])
            utils.mostrar_tablero(tablero_usuario)

    utils.sistema_de_turnos(tablero_usuario, tablero_maquina, flota_usuario, flota_maquina, modo)


