class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_leidas = 0

    def mostrar_libro(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Paginas: {self.paginas}")

    def leer(self, paginas):
        if self.paginas_leidas + paginas <= self.paginas:
            self.paginas_leidas += paginas
        else:
            self.paginas_leidas = self.paginas
        print (f"Leiste: {self.paginas_leidas} paginas")

    def progreso(self):
        if self.paginas == 0:
            return 0
        else:
            return(self.paginas_leidas / self.paginas) * 100

    @classmethod
    def cargar_desde_string(cls, libro_string):
        titulo, autor, paginas = libro_string.split(",")
        return cls(titulo, autor, int(paginas))
     
    @staticmethod
    def libro_grande(paginas):
        if paginas >= 500:
            print("Es un libro grande")
            return True
        else:
            print("Es un libro pequeño")
        return False