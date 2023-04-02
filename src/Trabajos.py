
import json


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
        self.id = 0
        self.__generaID()

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

    def __generaID(self):
        """Genera un ID de 4 digitos (5 de ser neceario)
            para el trabajador, con base en su puesto.
            Los operarios tienen un ID con 1 como primer dígito
            Los programadores tienen un ID con 2 como primer dígito
            Los administrativos tienen un ID con 3 como primer dígito
            Los jefes tienen un ID con 4 como primer dígito
        """
        
        try:
            with open("ficheros/contador.json", "r") as fichero:
                datos = json.load(fichero)
                fichero.close()
            self.__calcula_ID(datos)
            with open("ficheros/contador.json", "w") as fichero:
                json.dump(datos, fichero, indent=4)
                fichero.close()
                return    
        except FileNotFoundError:
            print("fichero no encontrado")  

    def __calcula_ID(self, datos: dict):
        """
        Método auxiliar que calcula el ID del empleado.
        """
        if self.puesto == "Operario":
            datos["Operario"] = datos["Operario"] + 1

            if datos["Operario"] < 998:
                self.id = 1000 + datos["Operario"]
            else:
                self.id = 10000 + datos["Operario"]  

        elif self.puesto == "Programador":
            datos["Programador"] = datos["Programador"] + 1

            if datos["Programador"] < 998:
                self.id = 2000 + datos["Programador"]
            else:
                self.id = 20000 + datos["Programador"]

        elif self.puesto == "Administrativo":
            datos["Administrativo"] = datos["Administrativo"] + 1
            if datos["Administrativo"] < 998:
                self.id = 3000 + datos["Administrativo"]
            else:
                self.id = 30000 + datos["Administrativo"]

        elif self.puesto == "Jefe":
            datos["Jefe"] = datos["Jefe"] + 1

            if datos["Jefe"] < 998:
                self.id = 4000 + datos["Jefe"]
            else:
                self.id = 40000 + datos["Jefe"] 
        else:
            datos["Otro"] = datos["Otro"] + 1
            if datos["Otro"] < 998:
                self.id = 5000 + datos["Otro"]
            else:
                self.id = 50000 + datos["Otro"]

    def get_id(self):  
         return self.id

        
           
              


    


