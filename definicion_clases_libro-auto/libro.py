class Libro:
    def __init__(self, titulo, autor, año_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.isbn = isbn

    def presentar(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicacion: {self.año_publicacion}")


class Auto:
    def __init__ (self, marca, modelo, precio, color):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color

    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        print(f"Color: {self.color}")
    
    def encender(self):
        print(f"El auto {self.marca} {self.modelo} está encendido")
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} está acelerando")
    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} está frenando")
    def detenerse(self):
        print(f"El auto {self.marca} {self.modelo} está detenido")
