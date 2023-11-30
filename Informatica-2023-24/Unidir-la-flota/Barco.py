from random import randint
from numpy import *

class Barco:
    """Define la posición del barco, así como su estado, propiedades y acciones que puede realizar o, se le puede realizar"""

    def __init__(self,tamanyo):
        self.tamanyo = tamanyo
        self.posicion = []
    
    #Establece en que casilla empieza el barco
    def establecer_posicion(self,posiciones_bloqueadas):

        # Hasta establecer la posición
        while True:
            # Posiciones ocupadas originalmente
            
            # Establece la posición inicialny la orientación
            posicion_inicial, orientacion = self.establecer_posicion_inicial()

            posiciones = self.comprobar_posiciones_barco(posicion_inicial=posicion_inicial,orientacion=orientacion, posiciones_bloqueadas=posiciones_bloqueadas) 

            # Si en barco esta en una casilla bloqueada, repetimos la asignación de posiciones
            if not posiciones is False:
                
                self.anyadir_posiciones_bloqueadas(barco=posiciones, bloqueadas=posiciones_bloqueadas)

                self.posicion = posiciones

                break
        

    def establecer_posicion_inicial(self):
        while True:
            posicion_inicial = [rand_posicion_linia(),rand_posicion_linia()]

            # Elige si el resto del barco se va a ubicar en OX o OY
            orientacion = randint(0,1)
            posicion_final_eje = posicion_inicial[orientacion] + self.tamanyo
            if(posicion_final_eje < 9):
                return posicion_inicial, orientacion

    # Comprueba sí en las casillas del barco estan bloqueadas
    def comprobar_posiciones_barco(self,posicion_inicial, orientacion, posiciones_bloqueadas):

        # Posiciones en las que se va a poner el barco

        posiciones = []

        for i in range(0, self.tamanyo):

            nueva_posicion = posicion_inicial.copy()
            nueva_posicion[orientacion] = nueva_posicion[orientacion] + i

            if tuple(nueva_posicion) in posiciones_bloqueadas:
                return False
                  
            posiciones.append(nueva_posicion)

        return posiciones          

    # Anyade al set de posiciones bloqueadas
    def anyadir_posiciones_bloqueadas(self, barco, bloqueadas):
        
        def encontrar_casilla(casilla,ar,de):
            cas = casilla.copy()
            cas[0] += ar
            cas[1] += de

            return tuple(cas)
        
        for posicion in barco:

            # Añade las posiciones bloqueadas por la presencia del barco (izquierda, derecha, arriba, abajo, centro)
            bloqueadas.add(tuple(posicion))
            bloqueadas.add(encontrar_casilla(posicion,0,1))
            bloqueadas.add(encontrar_casilla(posicion,0,-1))
            bloqueadas.add(encontrar_casilla(posicion,1,0))
            bloqueadas.add(encontrar_casilla(posicion,-1,0))

    #Comprueba si el barco sigue activo y si es así devuelve el tamanyo
    def activo(self):

        if len(self.posicion) != 0:
            return self.tamanyo
        
        return False

    def ser_atacado(self, casilla):
        if casilla in self.posicion:
            self.posicion.remove(casilla)
            if len(self.posicion) == 0:
                print("TOCADO Y HUNDIDO")
            else:
                print("TOCADO")
            return True
        
        return False


def rand_posicion_linia():
    return randint(0,9)


