# Alejandro Ortega Maldonado
def product_table(number):
    with open(f"tabla-{number}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{number} x {i} = {number * i}\n")

while True:
    try:
        number = int(input("Ingrese un número entero entre 1 y 10: "))
        if 1 <= number <= 10:
            break
        else:
            print("Número fuera de rango. Intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

product_table(number)
print(f"Se ha creado el archivo 'tabla-{number}.txt' con la tabla de multiplicar.")
