# 1. Apertura del archivo
fichero = open(
    '/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/24_archivos.txt')
 
# 2. Lectura de todo el fichero
linea = fichero.readline()
print(type(linea))
print("---"*30)

print(linea) #Imprime la primera línea
print(fichero.readline()) #Imprime la segunda línea
print(fichero.readline()) #Imprime la tercera línea
print(fichero.readline()) #Imprime la cuarta línea


# 3. Cierre de archivo.

fichero.close()

