# Alejandro Ortega Maldonado

from Model import PetCard


# Lista vacía para almacenar las fichas de mascotas
BDPetCards = []

# Función para obtener una ficha por número de socio
def get_pet_card():

    
    member_number = int(input("Insert a member number: "))
    
    # Recorre la lista de fichas de mascotas
    for card in BDPetCards:

        # Si se encuentra una ficha con el número de socio ingresado
        if card.member_number == member_number:

            # Se imprime ficha encontrada
            print("_________________________________")
            print("Found card:", "\n")
            print(f"Member Number: {card.member_number}", "\n")
            print(f"Pet's Name: {card.pet_name}", "\n")
            print(f"Pet Type: {card.pet_type}", "\n")
            return
        
    # Si no se encuentra ficha
    print("This member number doesn't exist or has a typo.")



# Función para agregar nueva ficha
def set_pet_card(pet_card):

    # Se agrega la ficha de mascota recibida como parámetro a la lista BDFichasMascotas
    BDPetCards.append(pet_card)


# Función para crear nueva ficha
def new_card():
    member_number = int(input("Insert Member Number: "))
    pet_name = input("Insert Pet's Name: ")
    pet_type = input("Insert Pet Type: ")
    pet_card = PetCard(member_number, pet_name, pet_type)
    set_pet_card(pet_card)

# Función para imprimir todas las fichas
def print_cards():
    print("_________________________________")
    print("| Pet Cards List |")
    print("_________________________________")
    print()

    for card in BDPetCards:
        print("Member Number:", card.member_number, "\n")
        print("Pet's Name:", card.pet_name, "\n")
        print("Pet Type:", card.pet_type, "\n")
    print("_____________________________________") 

