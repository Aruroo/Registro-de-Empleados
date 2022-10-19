from Trabajos import Trabajador
from Registro import Registro

class Perfil(Registro):

    def __init__(self,trabajador: Trabajador):
        """
            Clase para crear un perfil con los datos del trabajador y 
            otros datos de interés.
            El trabajador tiene que estar previamente registrado en el sistema.
        """
        self.trabajador = trabajador
        

    def genera_perfil(self)-> str:
        """
            Genera un String con los datos procesados del trabajador separados
            un salto de línea. 
        """
        perfil = "ID" + str(self.trabajador.id) + "\n"
        perfil += "Nombre: " + self.trabajador.nombre + "\n"
        perfil += "Apellido: " + self.trabajador.apellido + "\n"
        perfil += "Puesto: " + self.trabajador.puesto + "\n"
        perfil += "RFC: " + self.trabajador.rfc + "\n"
        perfil += "CURP: " + self.trabajador.curp + "\n"
        


        

