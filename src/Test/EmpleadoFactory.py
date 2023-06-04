import sys
sys.path.append('../src')
from faker import Faker
import random
from Trabajos import Trabajador
from Registro import Registro

class EmpleadoFactory():
    """
    Clase que crea empleados ficticios para la aplicacion.
    """
    def __genera_RFC(self,nombre:str, apellido:str):
        """
        Genera el RFC del empleado ficticio
        """
        return apellido[:2] + nombre[:2] + str(random.randint(1000, 9999))

    def __genera_CURP(self, nombre:str, apellido:str):
        """
        Genera el CURP del empleado ficticio
        """
        return apellido[:2] + nombre[:2] + str(random.randint(1000, 9999))

    def __puesto_aleatorio(self)->str:
        """
        Genera un puesto aleatorio para el empleado ficticio.
        Cada puesto tiene una probabilidad diferente.
        En general, las probabilidades son las siguientes:
        Jefe: 10%
        Administrativo: 20%
        Operario: 50%
        Programador: 10%
        Otro: 10%
        """
        puestos = ["Jefe", "Administrativo", "Operario", "Programador", "Otro"]
        probabilidades = [0.1, 0.2, 0.5, 0.1, 0.1]
        return random.choices(puestos, probabilidades)[0] # random.choices regresa una lista, por eso el [0]


    def crea_empleados(self):
        """
        Crea empleados ficticios para la aplicacion.
        """
        faker = Faker()
        registro = Registro()
        for i in range(100):
            nombre = faker.first_name()
            apellido = faker.last_name()
            puesto = self.__puesto_aleatorio()
            salario = random.randint(10, 30)
            trabajador = Trabajador(nombre, apellido, salario, puesto)
            rfc = self.__genera_RFC(nombre, apellido)
            curp = self.__genera_CURP(nombre, apellido)
            trabajador.set_RFC(rfc)
            trabajador.set_CURP(curp)
            registro.agregar_trabajador(trabajador)

if __name__ == "__main__":
    factory = EmpleadoFactory()
    factory.crea_empleados()