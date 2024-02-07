# Miguel Ángel Roldán de Haro

from Model import FichaMascota


# Lista vacía para almacenar las fichas de mascotas
BDFichasMascotas = []

# Función para obtener una ficha por número de socio
def get_Ficha_Mascota():

    
    numero_socio = int(input("Ingrese el número de socio: "))
    
    # Recorre la lista de fichas de mascotas
    for ficha in BDFichasMascotas:

        # Si se encuentra una ficha con el número de socio ingresado
        if ficha.num_socio == numero_socio:

            # Se imprime ficha encontrada
            print("_________________________________")
            print("Ficha encontrada:", "\n")
            print(f"Número de Socio: {ficha.num_socio}", "\n")
            print(f"Nombre de la Mascota: {ficha.nombre_mascota}", "\n")
            print(f"Tipo de Mascota: {ficha.tipo_mascota}", "\n")
            return
        
    # Si no se encuentra ficha
    print("El número de usuario no es válido o no existe.")



# Función para agregar nueva ficha
def set_Ficha_Mascota(ficha_mascota):

    # Se agrega la ficha de mascota recibida como parámetro a la lista BDFichasMascotas
    BDFichasMascotas.append(ficha_mascota)


# Función para crear nueva ficha
def Ficha_nueva():
    num_socio = int(input("Ingrese el número de socio: "))
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    tipo_mascota = input("Ingrese el tipo de mascota: ")
    ficha_mascota = FichaMascota(num_socio, nombre_mascota, tipo_mascota)
    set_Ficha_Mascota(ficha_mascota)

# Función para imprimir todas las fichas
def Imprimir_Fichas():
    print("_________________________________")
    print("| Listado de Fichas de Mascotas |")
    print("_________________________________")
    print()

    for ficha in BDFichasMascotas:
        print("Número de Socio:", ficha.num_socio, "\n")
        print("Nombre de la Mascota:", ficha.nombre_mascota, "\n")
        print("Tipo de Mascota:", ficha.tipo_mascota, "\n")
    print("_____________________________________") 

