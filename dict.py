entrada_claves = input("Ingresa las claves separadas por comas: ")
entrada_valores = input("Ingresa los valores separados por comas: ")

# convierte las cadenas de entrada en listas
claves = entrada_claves.split(',')
valores = entrada_valores.split(',')

# listas con la misma longitud
if len(claves) == len(valores):
    # crea el diccionario usando la función zip y dict
    diccionario = dict(zip(claves, valores))
    print("Diccionario creado:", diccionario)
else:
    print("Error: El número de claves y valores no coincide.")
