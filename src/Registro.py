import json
import time
from Trabajos import Trabajador
class Registro():

    def __init__(self):
        """
        Constructor de la clase
        """
        self.__trabajadores = {}

    def agregar_trabajador(self, trabajador: Trabajador):
        """
        Agrega un trabajador al diccionario de trabajadores, con su ID como llave
        """
        self.__trabajadores[trabajador.id] = trabajador.__dict__()
        #agregamos la fehca de alta
        self.__trabajadores[trabajador.id]["fecha_registro"] = time.strftime("%d/%m/%Y")
        

    def __necesita_almacenarse(self):
        """
        Checa si hay trabajadores que necesiten ser almacenados
        """
        return len(self.__trabajadores) > 0   

    def almacena_trabajadores(self):
        """
        Almacena los trabajadores en un fichero
        """
        if self.__necesita_almacenarse():
            #checamos si el fichero ya existe
            try:
                with open("ficheros/trabajadores.json", "r") as fichero:
                    datos = json.load(fichero)
                    fichero.close()
                for trabajador in self.__trabajadores:
                        if trabajador not in datos:
                            datos[trabajador] = self.__trabajadores[trabajador]
                with open("ficheros/trabajadores.json", "w") as fichero:
                    json.dump(datos, fichero, indent=4)
                    fichero.close()
                    return
        
            except FileNotFoundError:
                #si no existe, lo creamos
                with open("ficheros/trabajadores.json", "w") as fichero:
                    json.dump(self.__trabajadores, fichero, indent=4)
                fichero.close()    
                return
        else:
            print("No hay trabajadores que almacenar")
            return
        
    
    def muestra_trabajadores(self)->dict:
        """
        Muestra los trabajadores almacenados en el fichero
        """
        try:
            with open("ficheros/trabajadores.json", "r") as fichero:
                datos = json.load(fichero)
                fichero.close()
            return datos
        except FileNotFoundError:
            print("Error", "No hay trabajadores almacenados")
            return {}
 