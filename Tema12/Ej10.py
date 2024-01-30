# Alejandro Ortega Maldonado
def calculate_invoice_total_value(quantity_no_IVA, percentage_IVA=21):
    total = quantity_no_IVA + (quantity_no_IVA * percentage_IVA / 100)
    return total


try:
    quantity_no_IVA = float(input("Ingrese la cantidad sin IVA: "))
    result = calculate_invoice_total_value(quantity_no_IVA)
    print(f"El total de la factura es: {result}")
except ValueError:
    print("Por favor, ingrese una cantidad válida.")
