import requests
import json

# parametros
name = input("Ingrese nombre")

# url del API REST
url = "https://api.nationalize.io/?name=" + name

# invoca el servidor web
# se recibe en un diccionario
result = requests.get(url).json()

# muestra el resultado
print(json.dumps(result, indent=4))
