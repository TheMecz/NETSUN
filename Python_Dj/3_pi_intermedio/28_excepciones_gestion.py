# ZeroDivitionError
try:
    resulado = 10 * (1/0)
except:
    print("Error de ZeroDivitionError")
    
# NameError
try:
    print(4 + spam*3)
except:
    print("Error de NameError")
    
# TypeError
try:
    print(resultado = "2" + 2)
except:
    print("Error de TypeError")
    
print("Hemos gestionado las excepciones")