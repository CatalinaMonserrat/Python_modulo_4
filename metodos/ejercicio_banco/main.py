"""main.py"""
from banco import CuentaBancaria

if __name__ == "__main__":

    cuenta1 = CuentaBancaria("Juan", 0)
    cuenta2 = CuentaBancaria("Pedro", 2000)
    cuenta3 = CuentaBancaria.cargar_desde_string("Jose, 5000")

    cuenta1.mostrar_datos()
    cuenta1.depositar(200)
    cuenta1.retirar(500)
    cuenta1.imprimir_saldo()

    print("\n" + "-" * 50 + "\n")

    cuenta2.mostrar_datos()
    cuenta2.depositar(1000)
    cuenta2.retirar(500)
    cuenta2.imprimir_saldo()

    print("\n" + "-" * 50 + "\n")

    cuenta3.mostrar_datos()
    cuenta3.depositar(1000)
    cuenta3.retirar(500)
    cuenta3.imprimir_saldo()