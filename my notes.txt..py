# Abrir el archivo en modo escritura (creará el archivo si no existe)
with open('my_notes.txt', 'w') as file:
    # Escribir tres líneas de notas en el archivo
    file.write("augusto alejandro heredia castillo.\n")
    file.write("programacion es lo mejor.\n")
    file.write("¡Programar es dificil!")

# Abrir el archivo en modo lectura
with open('my_notes.txt', 'r') as file:
    # Leer el archivo línea por línea
    for line in file:
        # Imprimir cada línea en la consola
        print(line.rstrip())  # rstrip() elimina los espacios en blanco al final de la línea

# El archivo se cierra automáticamente al salir del bloque with