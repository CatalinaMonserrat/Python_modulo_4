from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, color,ruedas):
        super().__init__(color,ruedas)

    def encender_motor(self):
        print("El motor esta encendido")