from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas):
        super().__init__(color, ruedas)

    def pedalear(self):
        print("Comenzaste a pedalear")

    