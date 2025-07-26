from tarjeta import TarjetaCredito

if __name__ == "__main__":

#Crear tarjetas 
    tarjeta1 = TarjetaCredito(1000, 0.15, 500)
    tarjeta2 = TarjetaCredito(2000, 0.1, 1000)
    tarjeta3 = TarjetaCredito(3000, 0.08)

    print("\nTarjeta Masterplott\n")
    tarjeta1.compra(50).compra(200).pago(100).cobrar_interes().mostrar_info_tarjeta()

    print("\n" + "-" * 50 + "\n")

    print("\nTarjeta MundoVisa\n")
    tarjeta2.compra(100).compra(200).compra(150).pago(50).pago(80).cobrar_interes().mostrar_info_tarjeta()

    print("\n" + "-" * 50 + "\n")

    print("\nTarjeta PremiumBlack\n")
    tarjeta3.compra(1000).compra(1200).compra(600).compra(150).compra(250).mostrar_info_tarjeta()

    print("\n" + "-" * 50 + "\n")

    TarjetaCredito.mostrar_todas_las_tarjetas()