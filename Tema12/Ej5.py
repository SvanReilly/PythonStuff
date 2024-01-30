# Alejandro Ortega Maldonado
quantity = float(input("Ingrese la cantidad a invertir: "))
year_interest = float(input("Ingrese el interés anual: "))
years = int(input("Ingrese el número de años: "))

for i in range(years):
    quantity *= (1 + year_interest / 100)
    print(f"Año {i + 1}: {quantity:.2f}")
