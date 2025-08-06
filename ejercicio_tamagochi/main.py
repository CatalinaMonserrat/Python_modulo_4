from tamagotchi import Tamagotchi
from persona import Persona
from tamagochi_dragon import Dragon

#Crear tamagotchi
Mascota1 = Tamagotchi("Pinky", "Rosa")
#Crear persona
p1 = Persona("Lucia", "Ramírez", Mascota1)

p1.jugar_con_tamagotchi()
print("\n")
p1.darle_comida()
print("\n")
p1.curar_tamagotchi()
print("\n")

#creando tamagochi especial
Mascota2 = Dragon("Tairn", "negro", "Lanzar fuego")
#Crear persona
p2 = Persona("Diego", "Garcia", Mascota2)

p2.jugar_con_tamagotchi()
print("\n")
Mascota2.usar_superpoder()