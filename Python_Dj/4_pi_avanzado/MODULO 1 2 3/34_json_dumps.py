import json

# leer archivo JSON
with open('/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/33_universidades.json', 'r') as json_file:
    data = json.load(json_file) # leer el archivo JSON
    
print(json.dumps(data, indent=2)) # Crea una cadena de texto en formato JSON