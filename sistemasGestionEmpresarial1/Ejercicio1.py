# Alejandro Ortega Maldonado

lista = [1, 2, "árbol", 5, 1.5, 6, "a"]

numeros = [elemento for elemento in lista if type(elemento) in [int, float]]
if numeros:
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"Número mayor: {maximo}, Número menor: {minimo}")
else:
    print("No hay números en la lista.")
