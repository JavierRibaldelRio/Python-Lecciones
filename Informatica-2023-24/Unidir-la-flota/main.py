from Barco import Barco
from imprimir_tablero import imprimir_tablero
from numpy import *
from os import system


def main(): 
    global barcos
    barcos = establecer_barcos()
    
    global tablero
    tablero = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Turnos que lleva el jugador
    global turnos
    turnos = 0

    global casillas_atacadas
    casillas_atacadas = []

    while True:
        imprimir_tablero(tablero)
        
        restantes = barcos_restantes()

        if (len(restantes) == 0):
            break
        atacar()
        turnos += 1

    print("¡ENHORABUENA HAS GANADO!, EN",turnos, "TURNOS")

        

# Obtiene las posiciones de los barcos

def establecer_barcos():
    # Crea un set
    posiciones_reservadas = set()

    barcos = []

    for i in [5,4,3,3,2,2,2]:

        barca = Barco(i)

        barca.establecer_posicion(posiciones_bloqueadas=posiciones_reservadas)

        barcos.append(barca)

    return barcos


def barcos_restantes():

    barcos_activos = []

    print("Tamaños barcos activos: ", end="")

    for barco in barcos:
        esta_activo = barco.activo()
        if not esta_activo == False:
            barcos_activos.append(esta_activo)

    print(barcos_activos)

    print("Turnos:", turnos)
    
    return barcos_activos

    
    
def atacar():
    casilla = obtener_casilla_ataque()
    disparar(casilla)
    
    
# Pregunta al usuario cual es la casilla de ataque
def obtener_casilla_ataque():

    while True:
        casilla = input("Posición a atacar (A1):")

        if len(casilla) == 2 and casilla[0].isalpha()  and casilla[1].isnumeric() and 0 <= int(casilla[1]) <=9 :
            columna = ord(casilla[0].upper())- ord("A")
            if 0 <= columna <= 9:
                fila = int(casilla[1])

                if [fila,columna]not in casillas_atacadas:
                    return [fila, columna]

            
        system("clear")

        print("Posición Incorrecta")
        imprimir_tablero(tablero)
        barcos_restantes()



def disparar(casilla):
    system("clear")
    for barco in barcos:
        if barco.ser_atacado(casilla):
            tablero[casilla[0]][casilla[1]] = 2
            return
    
    print("AGUA")
    tablero[casilla[0]][casilla[1]] = 1



if __name__ == "__main__":
    main()