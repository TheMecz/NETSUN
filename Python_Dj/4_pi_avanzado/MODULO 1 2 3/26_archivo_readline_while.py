fichero = open(
    '/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/24_archivos.txt')
oracion = fichero.readline()
while oracion != "":
    print(oracion, end="")
    oracion = fichero.readline()
    