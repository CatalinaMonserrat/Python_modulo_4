class Tamagotchi:
    def __init__(self, nombre, color, salud = 100, felicidad = 100, energia = 100):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def mostrar_estatisticas(self):
        print(f"Nombre: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Salud: {self.salud}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Energia: {self.energia}")
    
    def jugar(self):
        if self.salud < 5:
            print(f"El tamagotchi {self.nombre} está enfermo, su salud es {self.salud} y no puede jugar.")
            return
        
        self.felicidad = min(self.felicidad + 10, 100) #aumenta la felicidad en 10
        self.salud = max(self.salud - 5, 0) #disminuye la salud en 5
        self.energia = max(self.energia - 10, 0) #disminuye la energia en 10

        print(f"El tamagotchi {self.nombre} está jugando. Valores actuales: felicidad {self.felicidad}, salud {self.salud} y energia {self.energia}.")

    def comer(self):
        self.salud = min(self.salud + 10, 100) #aumenta la salud en 10
        self.felicidad = min(self.felicidad + 5, 100) #aumenta la felicidad en 5
        self.energia = min(self.energia + 5, 100) #Aumneta la energia en 5
        print(f"El tamagotchi {self.nombre} está comiendo, Sus valores actualizados son: salud {self.salud}, energia {self.energia} y felicidad {self.felicidad}.")

    def curar(self):
        self.salud = min(self.salud + 20, 100) #aumenta la salud en 20
        self.felicidad = max(self.felicidad - 5, 0) #disminuye la felicidad en 5
        self.energia = max(self.energia - 15, 0) #disminuye la energia en 10
        print(f"El tamagotchi {self.nombre} está curandose. Sus valores actuales son: salud {self.salud}, energia {self.energia} y felicidad {self.felicidad}.")