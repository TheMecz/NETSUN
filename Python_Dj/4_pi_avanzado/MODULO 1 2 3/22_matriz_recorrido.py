matriz = []

row = 4
colum = 6

#Llenar matriz
for i in range(row):
    fila = [0] * colum
    matriz.append(fila)

# Recorrer matriz
print("Recorrido de matriz por medio de For")

for i in range(row):
    for j in range(colum):
        print(matriz[i][j], end=" ")
    print()