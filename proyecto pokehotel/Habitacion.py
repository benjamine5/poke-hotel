class habitacion:
    def __init__(self,posicion,disponibilidad,precio,tiempoEstadia):
        self.posicion=posicion
        self.disponibilidad=disponibilidad
        self.precio=precio
        self.tiempoEstadia=tiempoEstadia




    #Geters
    def get_posicion(self):
        return self.posicion

    def get_disponibilidad(self):
        return self.disponibilidad

    def get_precio(self):
        return self.precio

    def get_tiempoEstadia(self):
        return self.tiempoEstadia
    #Setters
    def set_posicion(self,posicion):
        self.posicion = posicion

    def set_disponibilidad(self,disponibilidad):
        self.disponibilidad = disponibilidad

    def set_precio(self,precio):
        self.precio = precio

    def set_tiempoEstadia (self,tiempoEstadia):
        self.tiempoEstadia = tiempoEstadia
