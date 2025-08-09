# Abrir un archivo para leer
file = open("mi_archivo.txt", "r")

# Leer todo el contenido del archivo
contenido = file.read()

# Imprimir el contenido leído
print(contenido)

# Cerrar el archivo
file.close()