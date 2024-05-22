fichero = open(
    '/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/30_archivos_write_for.txt', 'w')

# Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Plátano"]

# Guardamos la lista en el fichero
for linea in lista:
    fichero.write(linea + "\n")

# Cerramos fichero.
fichero.close()