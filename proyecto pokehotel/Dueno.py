class dueno:
    def __init__(self,nombre,edad,Rut,numeroTelefono):
        self.nombre=nombre
        self.edad=edad
        self.Rut=Rut
        self.numeroTelefono=numeroTelefono



    #Geters
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_Rut(self):
        return self.Rut

    def get_numeroTelefono(self):
        return self.numeroTelefono
    #Setters
    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_edad(self,edad):
        self.edad = edad

    def set_Rut(self,Rut):
        self.Rut = Rut

    def set_tnumeroTelefono (self,numeroTelefono):
        self.numeroTelefono = numeroTelefono
