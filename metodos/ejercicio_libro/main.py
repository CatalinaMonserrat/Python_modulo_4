"""main.py"""
from libro import Libro

if __name__ == "__main__":

    libro1 = Libro("El senor de los anillos", "JRR Tolkien", 600)
    libro2 = Libro("Harry Potter y la piedra filosofal", "JK Rowling", 300)
    libro3 = Libro.cargar_desde_string("It, Stephen King, 800")

    libro1.mostrar_libro()
    libro1.leer(100)
    libro1.progreso()

    libro2.mostrar_libro()
    libro2.leer(200)
    libro2.progreso()

    libro3.mostrar_libro()
    libro3.leer(300)
    libro3.progreso()

    Libro.libro_grande(600)