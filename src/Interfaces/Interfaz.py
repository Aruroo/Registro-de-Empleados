import sys
sys.path.append('../src')
sys.path.append('../Interfaz')
from MuestraTrabajadores import MuestraTrabajadores
from RegistroInterfaz import RegistroInterfaz
from tkinter import*
from tkinter import ttk


class Interfaz():
    
    def __init__(self):
        """
        Clase que crea la interfaz de la aplicacion
        """
        self.raiz = Tk()
        self.raiz.title("Aplicacion de Empresa")
        self.raiz.geometry("1200x600")
        self.raiz.resizable(0,0)
        self.raiz.config(bg="white")
        self.__crea_saludo()
        self.__crea_botones_opciones()

    def __crea_saludo(self):
        """
        Crea el saludo inicial
        """
        saludo = Label(self.raiz, text="Bienvenido a la aplicacion de Empresa", font=("Arial", 20), bg="white")
        saludo.place(x=100, y=50)    

    def __crea_botones_opciones(self):
        """
        Crea un boton para agregar trabajadores y otro para mostrar los existentes,
        al presionarlas se ejecutan las funciones __registrar_nuevo_empleado y __muestra_trabajadores
        respectivamente
        """
        self.cuadro_registro = ttk.Frame(self.raiz)
        self.cuadro_mostrar = ttk.Frame(self.raiz)

        boton_reg = ttk.Button(self.raiz, text="Registrar nuevo empleado", command=self.__registrar_nuevo_empleado)
        boton_reg.place(x=100, y=150)

        boton_mos = ttk.Button(self.raiz, text="Mostrar empleados existentes", command=self.__muestra_trabajadores)
        boton_mos.place(x=450, y=150)
         
    def __registrar_nuevo_empleado(self):
        """
        Muestra un label que indica que se agreguen trabajadores,
        genera un desplegable con las opciones de trabajadores,
        establece los datos del trabajador y crea el boton para agregarlo
        """
        interfazDeRegistro = RegistroInterfaz(self.cuadro_registro)
        self.__cambia_frame(self.cuadro_registro)

        boton_mos = ttk.Button(self.raiz, text="Mostrar trabajadores existentes", command=self.__muestra_trabajadores)
        boton_mos.place(x=50, y=50)


    def __muestra_trabajadores(self):
        """
        Muestra los trabajadores existentes en el fichero en una tabla
        """
        interfazDeMuestra = MuestraTrabajadores(self.cuadro_mostrar)

        self.__cambia_frame(self.cuadro_mostrar)
        
        boton_reg = ttk.Button(self.raiz, text="Registrar nuevo empleado", command=self.__registrar_nuevo_empleado)
        boton_reg.place(x=50, y=50)

    def __cambia_frame(self, frame: ttk.Frame):
        """
        Cambia de frame
        """
        frame.place(x=0, y=0, width=1200, height=600)
        frame.tkraise()       

       
if __name__ == "__main__":
    Interfaz = Interfaz()
    Interfaz.raiz.mainloop()
       