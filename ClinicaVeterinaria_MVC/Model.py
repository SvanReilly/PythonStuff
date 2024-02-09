# Alejandro Ortega Maldonado

# Definición de la clase PetCard
class PetCard:

    # Constructor de la clase
    def __init__(self, member_number, pet_name, pet_type):

        # Inicialización de los atributos con los valores recibidos como parámetros
        # Self. es el aálogo de this (de Java) pero en Python
        self.member_number = member_number
        self.pet_name = pet_name
        self.pet_type = pet_type
