#Ejercicio Clase CuentaBancaria

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.mostrar_saldo = True

#Mostrar Datos
    def mostrar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        
# Depositar Monto
    def depositar(self, cantidad):
        print(f"Depositaste ${cantidad}.")
        self.saldo += cantidad

# Retirar Monto
    def retirar(self, cantidad):
        if self.saldo < cantidad:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            self.saldo -= cantidad
            print(f"Retiraste ${cantidad}.")

# Mostrar Saldo
    def imprimir_saldo(self):
        print(f"El saldo es: {self.saldo}")
    
    @classmethod
    def cargar_desde_string(cls, cuenta_string):
        titular, saldo = cuenta_string.split(",")
        return cls(titular, int(saldo))