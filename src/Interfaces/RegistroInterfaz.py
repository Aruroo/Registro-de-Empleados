import sys
sys.path.append('../src')
from PIL import Image
from PIL import ImageTk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter import filedialog
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
        self.__imagen_def =Image.open("../src/ficheros/imagenes/default.jpg")
        self.__crea_imagen(self.__imagen_def)
        self.__agrega_trabajador_Label()
        self.__desplegable_opciones_trabajador()
        self.__establece_datos_trabajador()
        self.__crea_boton_agregar()
        self.__boton_agrega_imagen()
            

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


    def __boton_agrega_imagen(self):
        """
        Crea el boton para agregar una imagen
        """
        boton_agregar_imagen = Button(self.cuadro_registro, text="Agregar imagen", font=("Arial", 15), bg="white", command=self.__carga_imagen)
        boton_agregar_imagen.place(x=50, y=420)

    def __carga_imagen(self):
        """
        Carga la imagen del trabajador
        """
        ruta_imagen = self.__explorador_imagenes()
        if ruta_imagen == "":
            return
        else: 
            self.__imagen_def = Image.open(ruta_imagen)
            imagen = Image.open(ruta_imagen)
        self.__crea_imagen(imagen)

    def  __crea_imagen(self, imagen:Image):
        """
        Muestra la imagen del trabajador a la izquierda.
        """
        imagen = imagen.resize((200, 200), Image.ANTIALIAS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = Label(self.cuadro_registro, image=imagen)
        imagen_label.image = imagen
        imagen_label.place(x=50, y=200)    
          

    def __explorador_imagenes(self) -> str:
        """
        Abre un explorador de archivos para que el usuario seleccione una imagen
        en formato PNG, JPG o JPEG.
        """
        ruta_imagen = filedialog.askopenfilename(initialdir = "/",
                                                title = "Selecciona una imagen",
                                                filetypes = (("png files","*.png"),
                                                ("jpg files","*.jpg"),
                                                ("jpeg files","*.jpeg")))
        return ruta_imagen

    def __agrega_imagen_ficheros(self,imagen:Image, id_trabajador:str):
        """
        Agrega una imagen del trabajador a la carpeta de ficheros/imagenes.
        """       
        imagen = imagen.resize((200, 200), Image.ANTIALIAS) 
        nombre_imagen = id_trabajador+ "." + imagen.format.lower()
        imagen.save("../src/ficheros/imagenes/"+nombre_imagen)
       
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
            
            # Creamos el trabajador
            self.trabajador = Trabajador(self.nombre.get(), self.apellido.get(), float(self.sueldo.get()), self.opciones.get())
            self.trabajador.set_RFC(self.rfc.get())
            self.trabajador.set_CURP(self.curp.get())
            
            # Registramos el trabajador
            nuevoRegistro = Registro()
            nuevoRegistro.agregar_trabajador(self.trabajador)
            self.__agrega_imagen_ficheros(self.__imagen_def, str(self.trabajador.get_id()))

            messagebox.showinfo("Agregado", "Trabajador agregado con exito")
            
            # Regresamos a los valores por defecto
            self.nombre.delete(0, END)
            self.apellido.delete(0, END)
            self.sueldo.delete(0, END)
            self.rfc.delete(0, END)
            self.curp.delete(0, END)
            self.opciones.set("")
            self.__imagen_def = Image.open("../src/ficheros/imagenes/default.jpg")
            self.__crea_imagen(self.__imagen_def)
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