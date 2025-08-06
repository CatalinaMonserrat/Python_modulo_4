from pelicula import Pelicula
from usuario import Usuario
from funcion import Funcion

class Administrador(Usuario):
   
    def agregar_pelicula(self, titulo, genero, duracion):
        return Pelicula(titulo,genero,duracion)
        
    def eliminar_pelicula(self, pelicula,lista_peliculas):
        if pelicula in lista_peliculas:
            lista_peliculas.remove(pelicula)

    def agregar_funcion(self, pelicula, fecha, hora, sala):
        return Funcion(pelicula,fecha, hora, sala)