#Crear un programa que permita ingresar los nombres de N alumnos y la cantidad M de cursos por alumnos.
N = int(input("Ingresar cantidad de estudiantes: "))
i = 1
while N >= i:
    nombre = input("Alumno {}: ".format(i))
    M = int(input("Ingresar cantidad de cursos: "))
    j = 0
    while M > j:
        curso_nombre = input("Cursos {}: ".format(j+1))
        j +=1
    i += 1
