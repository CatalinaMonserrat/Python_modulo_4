#Ejercicio Tarjeta de credito

class TarjetaCredito:
    """Atributos clase TajertaCredito"""
    tarjetas_creadas = []

    def __init__(self, limite_credito,intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas_creadas.append(self)

    def compra(self, monto):
        """Metodo compra"""
        if self.saldo_pagar + monto > self.limite_credito:
            print("No se puede realizar la compra")
        else:
            self.saldo_pagar += monto
            print(f"Ha realizado una compra por ${monto}. Saldo a pagar ${self.saldo_pagar}")
        return self

    def pago(self, monto):
        """Metodo pago"""
        if monto <= 0:
            print("El monto a pagar debe ser mayor que 0")
        elif monto > self.saldo_pagar:
            print(f"Esta intentando pagar más de lo que debe. Tu saldo es ${self.saldo_pagar}")
        else:
            self.saldo_pagar -= monto
            print(f"Ha realizado un pago por ${monto}. Nuevo Saldo: ${self.saldo_pagar}")
        return self

    def mostrar_info_tarjeta(self):
        """Metodo mostrar_info_tarjeta"""
        print(f"Limite de credito: ${self.limite_credito}")
        print(f"Intereses: {self.intereses * 100}%")
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        """Metodo cobrar_interes"""
        self.saldo_pagar += self.saldo_pagar * self.intereses
        print(f"Se han sumado los intereses. Nuevo Saldo: ${self.saldo_pagar:.2f}")
        return self

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        """Metodo mostrar_todas_las_tarjetas"""
        print("Listado de Tarjetas Registradas")
        for i, tarjeta in enumerate(cls.tarjetas_creadas, start=1):
            print(f"Tarjeta {i}")   
            tarjeta.mostrar_info_tarjeta()