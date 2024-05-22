fichero = open(
    '/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/31_archivos_writelines.txt', 'w')

lista = ["Manzana\n", "Pera\n", "Platano\n"]

fichero.writelines(lista)
fichero.close()