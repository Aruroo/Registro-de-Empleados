import random

class Trabajador():

    def __init__(self, nombre, apellido, sueldo: int , puesto):
        """
        Inicializa el trabajador
        """
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.puesto = puesto
        self.curp = ""
        self.rfc = ""

    def set_puesto(self, puesto):
        """Establece el puesto del trabajador
           puestos: jefe, administrativo, operario
        """
        self.puesto = puesto    

    def __str__(self):
        return "Nombre: " + self.nombre +" "+ self.apellido + " Sueldo: " + str(self.sueldo)

    def set_horas_trabajadas(self, horas):
        """Horas trabajadas por el trabajador en la semana
        """
        self.horas = horas

    def set_CURP(self, curp):
        """Establece la CURP del trabajador
        """
        self.curp = curp

    def set_RFC(self, rfc):
        """Establece el RFC del trabajador
        """
        self.rfc = rfc    

    def calcula_sueldo(self):
        """Calcula el sueldo del trabajador
            El sueldo se calcula en base a las horas trabajadas
        """
        return self.sueldo * self.horas

    def __dict__(self):
        return {"nombre": self.nombre,
                 "apellido": self.apellido,
                  "sueldo": self.sueldo, 
                  "puesto": self.puesto,
                  "RFC": self.rfc,
                  "CURP": self.curp,
                  }

    def generaID(self):
        """Genera un ID para el trabajador
        """
        self.id = random.randint(1000, 9999)
        return self.id    

class Jefe(Trabajador):

    def __init__(self, nombre, apellido, sueldo):
        super().__init__(nombre, apellido, sueldo)
        self.set_puesto("Jefe")


class Administrativo(Trabajador):
    
        def __init__(self, nombre, apellido, sueldo):
            super().__init__(nombre, apellido, sueldo)
            self.set_puesto("Administrativo")

class Operario(Trabajador):
        
            def __init__(self, nombre, apellido, sueldo):
                super().__init__(nombre, apellido, sueldo)
                self.set_puesto("Operario")
        
class Programador(Trabajador):
        
            def __init__(self, nombre, apellido, sueldo):
                super().__init__(nombre, apellido, sueldo)
                self.set_puesto("Programador")
    


    


