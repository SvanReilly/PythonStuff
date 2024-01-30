# Alejandro Ortega Maldonado
number = int(input("Ingrese un número entero positivo: "))
odds = [str(x) for x in range(1, number + 1) if x % 2 != 0]
print(", ".join(odds))
