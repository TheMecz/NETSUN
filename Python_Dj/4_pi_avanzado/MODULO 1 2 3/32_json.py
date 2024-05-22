# Json: JavaScript Object Notation
# Es uno de los foramtos ligeros más utilizados para el intercambio de datos.
# Resulta sencillo de leer y escribir, para los programadores y simple de interpretar y generar para las máquinas.

import json

# un objeto de tipo diccionario.

obj = {
    "Nombre": "Juan Perez",
    "Edad": 25,
    "Ciudad": "Lima"
}

# Guardar en un achivo JSON:

with open('/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/32_formato_json.json', 'w') as outfile:

# convertimos a JSON
    json.dump(obj, outfile)