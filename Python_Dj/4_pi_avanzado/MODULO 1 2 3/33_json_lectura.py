import json
with open('/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/33_universidades.json', 'r') as json_file:
    data = json.load(json_file)
    diccionario = data[0]
    #print(data) #El archivo json se volvió una lista
    print(diccionario)
    
    print("alpha_two_code:", diccionario["alpha_two_code"])
    print("domains:", diccionario["domains"])
    print("country:", diccionario["country"])
    print("web_pages:", diccionario["web_pages"])

