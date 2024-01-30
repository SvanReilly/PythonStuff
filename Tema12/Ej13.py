# Alejandro Ortega Maldonado
def apply_function_to_list(function, list):
    return [function(x) for x in list]

str_number = input("Ingrese una lista de números separados por espacios: ")
trial = [float(num) for num in str_number.split()]

def square(x):
    return x**2

result = apply_function_to_list(square, trial)
print(f"El resultado de aplicar la función a la muestra es: {result}")
