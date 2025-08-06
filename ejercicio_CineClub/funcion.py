class Funcion:
    def __init__(self, pelicula, fecha, hora, sala):
        self.pelicula = pelicula
        self.fecha = fecha
        self.hora = hora
        self.sala = sala
        self.asientos_disponibles = 50
        self.precio_boleto = 5000

    def mostrar_asientos(self):
        print(f"Asientos disponibles para la función de {self.pelicula.titulo}: {self.asientos_disponibles}")

    def reservar_asiento(self):
        if self.asientos_disponibles > 0:
            self.asientos_disponibles -= 1
            return True
        return False