# Alejandro Ortega Maldonado
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

try:
    number = int(input("Inserte un número entero positivo: "))
    if number < 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        result = factorial(number)
        print(f"El factorial de {number} es: {result}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
