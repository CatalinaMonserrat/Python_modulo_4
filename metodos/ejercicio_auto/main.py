"""main.py"""
from auto import Vehiculo

if __name__ == "__main__":

    auto1 = Vehiculo("Toyota", "Corolla", 20)
    auto2 = Vehiculo("Honda", "Civic", 0)
    auto3 = Vehiculo.crear_desde_texto("Susuki, Impreza, 50")

    auto1.mostrar_estado()
    auto1.acelerar(50)
    auto1.frenar (20)

    print("\n" + "-" * 50 + "\n")

    auto2.mostrar_estado()
    auto2.acelerar(0)
    auto2.frenar(10)

    print("\n" + "-" * 50 + "\n")

    auto3.mostrar_estado()
    auto3.acelerar(100)
    auto3.frenar(10)

    print("\n" + "-" * 50 + "\n")
    
    Vehiculo.evaluar_velocidad(auto1.velocidad)
    Vehiculo.evaluar_velocidad(auto2.velocidad)
    Vehiculo.evaluar_velocidad(auto3.velocidad)