d1 = {
    "Nombre": "Jorge",
    "Edad": 25,
    "Documento":10203040
}

print("---"*30)

# 1. Imprime los key del diccionario

for x in d1:
    print(x)
    
print("---"*30)
    
# 2. Imprime los value del diccionario
for x in d1:
    print(d1[x])

print("---"*30)

# 3. Imprime los key y value del diccionario
for x, y in d1.items():
    print(x,y)
    
print("---"*30)