# Alejandro Ortega Maldonado

def future_value_calculation(quantity, interest_tax, number_years):
    for i in range(number_years + 1):
        future_value = quantity * (1 + interest_tax / 100) ** i
        print(f"Año {i} : {future_value}")

def current_value_calculation(quantity, interest_tax, number_years):
    for i in range(number_years, -1, -1):
        current_value = quantity / (1 + interest_tax / 100) ** i
        print(f"Año {i} : {current_value}")


try:
    capital = float(input("Introduce un capital: "))
    interest_tax = float(input("Introduce un tipo de interés: "))
    number_years = int(input("Introduce un número de años: "))
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")

if capital > 0 and interest_tax >= 0 and number_years >= 0:
    print("VALOR FUTURO")
    future_value_calculation(capital, interest_tax, number_years)

    print("VALOR ACTUAL")
    current_value_calculation(capital, interest_tax, number_years)
else:
    print("Los valores ingresados deben ser positivos.")
