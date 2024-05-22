# No esta permitido la modificación porque es INMUTABLE

tupla = (1, 2, 3)
try:
    tupla[0] = 5  # Esto generará un TypeError
except:
    # Imprime el mensaje de error
    print("No se puede modificar una tupla.")

