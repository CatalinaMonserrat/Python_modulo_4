class Usuario:
    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self._contrasena = contrasena  # Atributo privado
        self.boletos = []

    def registrarse(self):
        print(f"El usuario {self.nombre} se ha registrado con el correo {self.email}")

    def comprar_boleto(self, funcion, asiento, precio):
        if funcion.reservar_asiento():
            from boleto import Boleto
            boleto = Boleto(codigo=f"B-{len(self.boletos) + 1}", funcion=funcion, asiento=asiento, precio=funcion.precio_boleto)
        
            self.boletos.append(boleto)
            return boleto
        else:
            print("No hay asientos disponibles")
            return None
