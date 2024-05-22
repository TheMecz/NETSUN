#Crear un programa que permita ingresar los nombres de N alumnos
N = int(input("Ingresar la cantidad de estudiantes: "))
i = 1
while N >= i:
    nombre = input("Nombre {}: ".format(i))
    i += 1
