# Crea un diccionario llamado "frutas" con las siguientes parejas clave-valor:
#               "manzana" - "roja"
#               "banana" - "amarilla"
#               "pera" - "verde"
#               "naranja" - "naranja"
# Imprime el diccionario "frutas" en la consola.
# Imprime el valor asociado a la clave "banana" en la consola.
# Imprime el valor asociado a la clave "uva" en la consola.

frutas = {
    "manzana":"roja",
    "banana":"amarilla",
    "pera":"verde",
    "naranja":"naranja"
}

print(frutas)
print(frutas.get("banana"))
print(frutas.get("uva"))
