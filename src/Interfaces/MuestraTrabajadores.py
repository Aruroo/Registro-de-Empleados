import sys
sys.path.append('../src')
from tkinter import*
from tkinter import ttk
from Registro import Registro

class MuestraTrabajadores():

    def __init__(self, cuadro_mostrar_empleados: ttk.Frame):
        """
            Clase auxiliar para mostrar los trabajadores existentes en el fichero
        """
        self.cuadro_mostrar_empleados = cuadro_mostrar_empleados
        self.__crea_tabla()


    def __crea_tabla(self):
        """
        Crea una tabla para mostrar los trabajadores
        """
        registro = Registro()
        trabajadores = registro.muestra_trabajadores()

        tabla = ttk.Treeview(self.cuadro_mostrar_empleados, columns=("ID","Nombre", "Apellido", "Sueldo", "Puesto", "Fecha de Registro"), show="headings")
        tabla.place(x=20, y=100)

        tabla.heading("ID", text="ID")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Apellido", text="Apellido")
        tabla.heading("Sueldo", text="Sueldo")
        tabla.heading("Puesto", text="Puesto")
        tabla.heading("Fecha de Registro", text="Fecha de Registro")

        for trabajador in trabajadores:
            nombre =trabajadores[trabajador]["nombre"]
            apellido = trabajadores[trabajador]["apellido"]
            sueldo = trabajadores[trabajador]["sueldo"]
            puesto = trabajadores[trabajador]["puesto"]
            fecha_registro = trabajadores[trabajador]["fecha_registro"]
            tabla.insert("", "end", values=(trabajador,nombre, apellido, sueldo, puesto, fecha_registro))  
