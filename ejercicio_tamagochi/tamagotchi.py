class Tamagotchi:
    def __init__(self, nombre, color, salud = 100, felicidad = 100, energia = 100):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        if self.salud < 5:
            print(f"El tamagotchi {self.nombre} está enfermo, su salud es {self.salud} y no puede jugar.")
            return
        
        self.felicidad = min(self.felicidad + 10, 100) #aumenta la felicidad en 10
        self.salud = max(self.salud - 5, 0) #disminuye la salud en 5
        print(f"El tamagotchi {self.nombre} está jugando. Su felicidad es {self.felicidad} y su salud es {self.salud}.")


    def comer(self):
        self.salud = min(self.salud + 10, 100) #aumenta la salud en 10
        self.felicidad = min(self.felicidad + 5, 100) #aumenta la felicidad en 5
        print(f"El tamagotchi {self.nombre} está comiendo y su salud es {self.salud} y su felicidad es {self.felicidad}.")

    def curar(self):
        self.salud = min(self.salud + 20, 100) #aumenta la salud en 20
        self.felicidad = max(self.felicidad - 5, 0) #disminuye la felicidad en 5
        print(f"El tamagotchi {self.nombre} está curandose y su salud es {self.salud} y su felicidad es {self.felicidad}.")