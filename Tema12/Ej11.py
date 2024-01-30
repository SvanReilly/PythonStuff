# Alejandro Ortega Maldonado
def calculate_average(trial):
    return sum(trial) / len(trial)

str_number = input("Ingrese una lista de números separados por espacios: ")
trial = [float(num) for num in str_number.split()]
average = calculate_average(trial)
print(f"La media de la muestra es: {average}")
