class pokemon:
    def __init__(self,nombre,altura,peso,tipo,sTipo):
        self.nombre=nombre
        self.altura=altura
        self.precio=peso
        self.tiempoEstadia=tipo





    #Geters
    def get_nombre(self):
        return self.nombre

    def get_disponibilidad(self):
        return self.altura

    def get_peso(self):
        return self.peso

    def get_tipo(self):
        return self.tipo
    def get_sTipo(self):
        return self.sTipo
    #Setters
    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_altura(self,altura):
        self.altura = altura

    def set_peso(self,peso):
        self.peso = peso

    def set_tipo (self,tipo):
        self.tipo = tipo

    def set_sTipo (self,sTipo):
        self.sTipo = sTipo