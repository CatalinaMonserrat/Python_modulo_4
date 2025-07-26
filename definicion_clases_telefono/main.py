"""main.py"""
from telefono import Telefono

if __name__ == "__main__":
    cel1 = Telefono("Nokia", "1100", 1000, "Negro", "1234567890")
    cel2 = Telefono("Samsung", "S20", 5000, "Blanco", "9876543210")

    cel1.info() 
    cel2.info()

    cel2.llamar(cel1.numero)
