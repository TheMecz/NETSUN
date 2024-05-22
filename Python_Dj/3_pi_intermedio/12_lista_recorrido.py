dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("utilozando for")
for item in dias:
    print(item)

print("utilizando range")
for i in range(len(dias)):
    print(dias[i])

print("utilizando enumerate")
for i, item in enumerate(dias):
    print(i, item)