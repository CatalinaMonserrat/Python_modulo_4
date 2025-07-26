class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

# Mostrar el estado del auto
    def mostrar_estado(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad: {self.velocidad}")

# Acelerar
    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"Acelerando a {self.velocidad} km/h")
# Frenar
    def frenar(self, cantidad):
        if self.velocidad == 0:
            print("El auto esta detenido")
        else:
            self.velocidad -= cantidad
            print(f"Frenando a {self.velocidad} km/h")
            
# Crear un auto desde texto
    @classmethod
    def crear_desde_texto(cls, texto):
            marca, modelo, velocidad = texto.split(",")
            return cls(marca, modelo, int(velocidad))

# Determinar si el auto es rapido
    @staticmethod
    def evaluar_velocidad(valor):
        if valor > 120:
            print("El auto es rapido")
        else: 
            print("El auto es lento")