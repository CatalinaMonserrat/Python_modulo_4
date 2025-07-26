"""definiendo clase telefono"""
class Telefono:
    def __init__(self, marca, modelo, precio, color, numero):
        #atributos
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.numero = numero
        #metodos
    def llamar(self, destino):
        print(f"Llamando desde {self.numero} al número {destino}")
        
    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        print(f"Color: {self.color}")


