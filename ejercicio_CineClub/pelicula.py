class Pelicula:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

    def obtener_info(self):
        return f"Título: {self.titulo}, Género: {self.genero}, Duración: {self.duracion}min"