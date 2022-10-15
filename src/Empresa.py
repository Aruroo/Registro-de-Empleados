
class Empresa():
    def __init__(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return self.nombre + ", " + self.direccion + ", " + self.telefono + ", " + self.email
      



    