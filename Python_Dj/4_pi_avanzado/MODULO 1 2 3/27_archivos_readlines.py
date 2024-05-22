fichero = open(
    '/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/24_archivos.txt')

lineas = fichero.readlines()
print(type(lineas))
print(lineas)

fichero.close()