from libro import Libro

if __name__ == "__main__":

    libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, "1234567890")
    libro2 = Libro("Harry Potter", "J.K. Rowling", 1997, "9876543210")
    libro3 = Libro("El hobbit", "J.R.R. Tolkien", 1937, "4567890123")
    libro4 = Libro("Cien años de soledad", "G. G. Márquez", 1967, "6543210987")
    libro5 = Libro("1984", "George Orwell", 1949, "7890123456")

    libro1.presentar()
    libro2.presentar()
    libro3.presentar()
    libro4.presentar()

from libro import Auto
if __name__ == "__main__":

    auto1 = Auto("Toyota", "Corolla", 20000, "Rojo")
    auto2 = Auto("Honda", "Civic", 25000, "Azul")

    auto1.info()
    auto2.info()
    auto1.encender()
    auto2.acelerar()
    auto1.frenar()
    auto2.detenerse()