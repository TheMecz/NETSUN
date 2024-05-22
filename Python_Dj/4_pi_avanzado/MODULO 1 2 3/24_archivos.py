# Un es archivo es un conjunto de bytes almacenados en un dispositivo
# Este dispositivo puede ser el disco duro de la PC, pero también podría ser un CD o la memoría de nuestro celular.
# Ejemplos comunes: Documentos de Word (docx), Excel (xsls), música (mp3), video (mp4), archivos de texto (txt)
# No son volátiles, es decir, permanecen aún cuando la PC está apagada.

#Existen 3 pasos para la creación de un Archivo

# 1. Apertura de archivo
fichero = open("/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/24_archivos.txt")
 
# 'r': Por defecto, para leer el fichero
# 'w': Para escribir en el fichero

# 2. Lectura de todo el fichero

print(fichero.read())

# 3. Cierre de archivo.

fichero.close()