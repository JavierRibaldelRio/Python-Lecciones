from random import randint
from numpy import *

class Barco:
    """Define la posición del barco, así como su estado, propiedades y acciones que puede realizar o, se le puede realizar"""

    def __init__(self,tamanyo):
        self.tamanyo = tamanyo
        self.posicion = []
    
    #Establece en que casilla empieza el barco
    def establecer_posicion(self,posiciones_ocupadas):
        print(posiciones_ocupadas)

    
        while True:
            # Posiciones ocupadas originalmente
            posi_ocupadas= posiciones_ocupadas.copy()
            # Alternativa al do while
            while True:
                posicion_inicial = [rand_posicion_linia(),rand_posicion_linia()]

                # Elige si el resto del barco se va a ubicar en OX o OY
                orientacion = randint(0,1)
                posicion_final_eje = posicion_inicial[orientacion] + self.tamanyo
                if(posicion_final_eje < 9):
                    break
            
            posiciones = []

            for i in range(0, self.tamanyo):

                nuevo = posicion_inicial.copy()
                nuevo[orientacion] = nuevo[orientacion] +i
                posiciones.append(nuevo)

            posi_ocupadas.extend(posiciones)
            if len(set(tuple(fil) for fil in posi_ocupadas)) == len(posi_ocupadas):
                self.posicion = posiciones
                return self.posicion        


            



def rand_posicion_linia():
    return randint(0,9)