from tamagotchi import Tamagotchi

class Dragon(Tamagotchi):
    def __init__(self, nombre, color, superpoder ,salud = 100, felicidad = 100, energia = 100):
        super().__init__(nombre, color, salud, felicidad, energia)
        self.superpoder = superpoder

    def usar_superpoder(self):
        if self.energia >= 20:
            self.energia = max(self.energia - 20, 0)
            print(f"El tamagotchi {self.nombre} ha lanzado su superpoder {self.superpoder}, su energia ahora es de {self.energia}.")
        else:
            print(f"El tamagotchi {self.nombre} no tiene suficiente energia para usar su superpoder")
