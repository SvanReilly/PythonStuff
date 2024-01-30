# Alejandro Ortega Maldonado
def squares_calculate(trial):
    return [x**2 for x in trial]

str_number = input("Ingrese una lista de números separados por espacios: ")
trial = [float(num) for num in str_number.split()]

cuadrados = squares_calculate(trial)
print(f"Los cuadrados de la muestra son: {cuadrados}")
