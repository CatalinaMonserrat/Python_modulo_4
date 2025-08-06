from administrador import Administrador
from usuario import Usuario
from pelicula import Pelicula
from funcion import Funcion

peliculas = []
funciones =[]
usuarios = []

#Administrador por defecto
admin = Administrador("Catalina", "admin@cineclub.cl", "admin1234")

# Crear películas por defecto
pelicula1 = admin.agregar_pelicula("El Hobbit", "Aventura", 180)
pelicula2 = admin.agregar_pelicula("El Conjuro", "Terror", 120)
peliculas.extend([pelicula1, pelicula2])

# Crear funciones por defecto
funcion1 = admin.agregar_funcion(pelicula1, "2025-08-12", "19:00", "Sala 1")
funcion2 = admin.agregar_funcion(pelicula2, "2025-08-13", "21:00", "Sala 2")
funciones.extend([funcion1, funcion2])

def menu_administrador():
    print("\nMenu Administrador:")
    while True:
        print("1. Agregar pelicula")
        print("2. Agregar funcion")
        print("3. Eliminar Pelicula")
        print("4. Ver funciones")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            titulo = input("Ingrese el titulo de la pelicula: ")
            genero = input("Ingrese el genero de la pelicula: ")
            duracion = int(input("Duración en minutos:"))
            nueva = admin.agregar_pelicula(titulo,genero,duracion)
            peliculas.append(nueva)
            print("Pelicula agregada con exito")
        
        elif opcion == "2":
            if not peliculas:
                print("No hay peliculas disponibles")
                continue
            print("Peliculas disponibles: ")
            for i, peli in enumerate(peliculas):
                print(f"{i+1}. {peli.titulo}")
            idx = int(input("Elige la película: ")) - 1
            peli = peliculas[idx]
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            hora = input("Ingrese la hora (HH:MM): ")
            sala = input("Ingrese la sala: ")
            nueva_funcion = admin.agregar_funcion(peli, fecha, hora, sala)
            funciones.append(nueva_funcion)
            print("Funcion agregada con exito")
        
        elif opcion == "3":
            if not peliculas:
                print("No hay peliculas registradas")
                continue

            for i, peli in enumerate(peliculas):
                print(f"{i+1}. {peli.titulo}")
            idx = int(input("Elige la película a eliminar: ")) - 1
            selecionada = peliculas[idx]
            admin.eliminar_pelicula(selecionada, peliculas)
            print("Pelicula eliminada con exito")

        elif opcion == "4":
            if not funciones:
                print("No hay funciones disponibles")
                continue
            for f in funciones:
                print(f"{f.pelicula.titulo} - {f.fecha} - {f.hora} - {f.sala}")
        
        elif opcion == "5":
            break

        else:
            print("Opcion no valida")

def menu_cliente(usuario):
    print(f"\n Bienvenido, {usuario.nombre}")
    while True:
        print("\n1. Ver funciones disponibles")
        print("2. Comprar boleto")
        print("3. Ver mis boletos")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            for i, f in enumerate(funciones):
                print(f"{i + 1}. {f.pelicula.titulo} - {f.fecha} {f.hora} en {f.sala}")
        
        elif opcion == "2":
            if not funciones:
                print("No hay funciones disponibles.")
                continue

            for i, f in enumerate(funciones):
                print(f"\n{i + 1}. {f.pelicula.titulo} - {f.fecha} {f.hora} en {f.sala} - ${f.precio_boleto}")

            idx = int(input("Elige la función: ")) - 1
            funcion = funciones[idx]

            print(f"Asientos disponibles: {funcion.asientos_disponibles}")
            cantidad = int(input("¿Cuántos boletos deseas comprar? "))

            if cantidad > funcion.asientos_disponibles:
                print("❌ No hay suficientes asientos disponibles.")
                continue

            for i in range(cantidad):
                asiento = input(f"Asiento para boleto #{i + 1}: ")

                boleto = usuario.comprar_boleto(funcion, asiento, funcion.precio_boleto)

                if boleto:
                    print(f"✅ Compraste Boleto {boleto.codigo} para {funcion.pelicula.titulo}")
        
        elif opcion == "3":
            if not usuario.boletos:
                print("No has comprado boletos aún.")
            else:
                for b in usuario.boletos:
                    print(f"{b.codigo} - {b.funcion.pelicula.titulo} en {b.asiento}")
       
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


# === Inicio del sistema ===

print("Bienvenido a CINECLUB")

tipo_usuario = input("¿Eres administrador o cliente? (a/c): ").lower()

if tipo_usuario == "a":
    correo = input("Correo: ")
    clave = input("Contraseña: ")
    if correo == admin.email and clave == admin._contrasena:
        menu_administrador()
    else:
        print("Acceso denegado.")
elif tipo_usuario == "c":
    print("\n Registro de cliente")
    nombre = input("Nombre: ")
    email = input("Correo: ")
    clave = input("Contraseña: ")
    usuario = Usuario(nombre, email, clave)
    usuarios.append(usuario)
    usuario.registrarse()
    menu_cliente(usuario)
else:
    print("Tipo de usuario no válido.")