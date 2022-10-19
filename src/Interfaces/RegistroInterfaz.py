import shutil
import sys
from tkinter import filedialog
import tkinter
sys.path.append('../src')
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from Registro import Registro
from Trabajos import Trabajador


class RegistroInterfaz():

    def __init__(self, cuadro_registro: ttk.Frame):
        """
           Clase auxiliar que crea la interfaz para agregar un trabajador
        """
        self.cuadro_registro = cuadro_registro
        self.trabajador = None
        self.__agrega_trabajador_Label()
        self.__desplegable_opciones_trabajador()
        self.__establece_datos_trabajador()
        self.__crea_boton_agregar()
            

    def __agrega_trabajador_Label(self):
        """
        Crea el label que indica que el usuario debe agregar un trabajador
        """
        agrega_trabajadorLab = Label(self.cuadro_registro, text="Agrega un trabajador", font=("Arial", 20), bg="light gray")
        agrega_trabajadorLab.place(x=515, y=100)

    def __desplegable_opciones_trabajador(self):
        """"
        Desplegable para elegir el tipo de trabajador
        """
        self.opciones = ttk.Combobox(self.cuadro_registro, values=["Jefe", "Administrativo", "Operario", "Programador"])
        self.opciones.place(x=515, y=150)
        self.opciones.config(state="readonly")

    def __establece_datos_trabajador(self):
        """
        Establece los datos del trabajador
        como nombre, apellido, sueldo y su respectivo label
        """
        nombreLab = Label(self.cuadro_registro, text="Nombre", font=("Arial", 15), bg="light gray")
        nombreLab.place(x=400, y=200)

        self.nombre = Entry(self.cuadro_registro)
        self.nombre.place(x=515, y=200)

        apellidoLab = Label(self.cuadro_registro, text="Apellido", font=("Arial", 15), bg="light gray")
        apellidoLab.place(x=400, y=250)

        self.apellido = Entry(self.cuadro_registro)
        self.apellido.place(x=515, y=250)

        sueldoLab = Label(self.cuadro_registro, text="Sueldo (por hora)", font=("Arial", 15), bg="light gray")
        sueldoLab.place(x=315, y=300)

        self.sueldo = Entry(self.cuadro_registro)
        self.sueldo.place(x=515, y=300)

        rfcLab = Label(self.cuadro_registro, text="RFC", font=("Arial", 15), bg="light gray")
        rfcLab.place(x=400, y=350)

        self.rfc = Entry(self.cuadro_registro)
        self.rfc.place(x=515, y=350)

        curpLab = Label(self.cuadro_registro, text="CURP", font=("Arial", 15), bg="light gray")
        curpLab.place(x=400, y=400)

        self.curp = Entry(self.cuadro_registro)
        self.curp.place(x=515, y=400)
        
    def __crea_boton_agregar(self):
        """
        Crea el boton para agregar un trabajador
        """
        boton_agregar = Button(self.cuadro_registro, text="Agregar", font=("Arial", 15), bg="white", command=self.__agrega_trabajador)
        boton_agregar.place(x=515, y=450)

    def __agrega_trabajador(self):
        """
        Agrega un trabajador a la lista de trabajadores, segun el tipo de trabajador
        Cuidando que los datos ingresados sean correctos
        """
        if self.__cuadros_vacios():
            messagebox.showerror("Error", "Debes llenar todos los campos")
            return

        if self.sueldo.get().isdigit() == False:
            messagebox.showerror("Error", "El sueldo debe ser un numero entero")
            return
            
        mensaje = messagebox.askquestion("Agregar", "¿Desea agregar a "+ self.nombre.get() + " " + self.apellido.get() + "?")

        if mensaje == "yes":

            self.trabajador = Trabajador(self.nombre.get(), self.apellido.get(), float(self.sueldo.get()), self.opciones.get())
            self.trabajador.set_RFC(self.rfc.get())
            self.trabajador.set_CURP(self.curp.get())
            
            nuevoRegistro = Registro()
            nuevoRegistro.agregar_trabajador(self.trabajador)
            nuevoRegistro.almacena_trabajadores()

            messagebox.showinfo("Agregado", "Trabajador agregado con exito")
            
            self.nombre.delete(0, END)
            self.apellido.delete(0, END)
            self.sueldo.delete(0, END)
            self.rfc.delete(0, END)
            self.curp.delete(0, END)
            self.opciones.set("")
        else:
            return

    def __cuadros_vacios(self):
        """
        Verifica que los cuadros de texto no esten vacios
        """
        if (self.nombre.get() == "" or self.apellido.get() == "" or self.sueldo.get() == ""
             or self.opciones.get() == "" or self.rfc.get() == "" or self.curp.get() == ""):
            return True
        else:
            return False


            

        


                       