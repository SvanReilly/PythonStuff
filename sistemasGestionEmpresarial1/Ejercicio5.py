# Alejandro Ortega Maldonado
import os
import locale


def decimal_a_binario(decimal):
    # Convertir el decimal a entero
    decimal_entero = int(decimal)
    binary = bin(decimal_entero)[2:]
    return binary


# Establecer la configuración regional para interpretar correctamente el separador decimal
locale.setlocale(locale.LC_NUMERIC, '')

# Obtener la ruta absoluta al archivo 'decimal.txt'
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'decimal.txt')

# Leer el contenido del archivo 'decimal.txt'
try:
    with open(file_path, 'r') as file_decimal:
        decimal_str = file_decimal.read().replace('\n', '')
        decimal = locale.atof(decimal_str)
except FileNotFoundError:
    print(f"El archivo '{file_path}' no se encuentra en la misma carpeta que el programa.")
    exit()
except ValueError:
    print(f"Error al convertir el valor decimal: '{decimal_str}' no es un número válido.")
    exit()

# Obtener el valor binario
binary_result = decimal_a_binario(decimal)

# Obtener la ruta completa del archivo 'binario.txt'
file_binario_path = os.path.join(current_directory, 'binario.txt')

# Escribir el resultado en el archivo 'binario.txt'
with open(file_binario_path, 'w') as file_binario:
    file_binario.write(binary_result)

print(f"El valor binario se ha guardado en 'binario.txt'.")
