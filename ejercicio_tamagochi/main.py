from tamagotchi import Tamagotchi
from persona import Persona
from tamagochi_dragon import Dragon

# Inicializar variables globales
p1 = None
Mascota = None
es_dragon = False

#Bienvenida
print("=== Bienvenido a Mascota virtual ===")
print("Por favor cree su usuario...")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Elección de mascota
print("=== Elige tu mascota Tamagotchi ===")
print("1. Tamagotchi normal")
print("2. Tamagotchi Dragon")

eleccion = int(input("Elige una opción: "))

if eleccion == 1:
    nombre_mascota = input("Ingrese el nombre de su Tamagotchi: ")
    color_mascota = input("Ingrese el color de su Tamagotchi: ")
    Mascota = Tamagotchi(nombre_mascota, color_mascota)
    p1 = Persona(nombre, apellido, Mascota)
    es_dragon = False

elif eleccion == 2:
    nombre_mascota = input("Ingrese el nombre de su Tamagotchi dragon: ")
    color_mascota = input("Ingrese el color de su Tamagotchi Dragon: ")
    superpoder = input("Ingrese el superpoder de su mascota: ")
    Mascota = Dragon(nombre_mascota, color_mascota, superpoder)
    p1 = Persona(nombre, apellido, Mascota)
    es_dragon = True
else:
    print("Opcion no valida, se asignara un Tamagotchi por defecto")
    Mascota = Tamagotchi("Pinky", "Rosa")
    persona = Persona(nombre, apellido, Mascota)
    es_dragon = False

    #Menú Interactivo 
def mostrar_menu():
    print("\n=== Bienvenido a Mascota virtual ===")
    print("1. Jugar con Tamagotchi")
    print("2. Darle de comer")
    print("3. Curarlo")
    print("4. Ver estado")
    if es_dragon:
        print("5. Usar superpoder")
        print("6. Salir")
    else:
        print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        p1.jugar_con_tamagotchi()
    elif opcion == "2":
        p1.darle_comida()
    elif opcion == "3":
        p1.curar_tamagotchi()
    elif opcion == "4":
        Mascota.mostrar_estatisticas()
    elif opcion == "5" and es_dragon:
        Mascota.usar_superpoder()
    elif (opcion == "5" and not es_dragon) or (opcion == "6" and es_dragon): 
        print("Gracias por jugar, saliendo del programa...")
        break   
    else:
        print("Opcion no valida, intente nuevamente.")