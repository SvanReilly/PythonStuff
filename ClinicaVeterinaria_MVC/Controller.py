# Alejandro Ortega Maldonado

from Model import PetCard
from colorama import *

# Lista vacía para almacenar las fichas de mascotas
BDPetCards = []


# Función para obtener una ficha por número de socio
def get_pet_card(member_number):
    show_me_pet_list = []

    for card in BDPetCards:
        if card.member_number == member_number:
            # Almacenar una tupla (nombre, tipo) en lugar de solo el nombre
            show_me_pet_list.append((card.pet_name, card.pet_type))

    # Concatenar el nombre y el tipo de mascota en la cadena vertical
    vertical_list = "\n\n".join(f"Name:{pet_name} \nType: {pet_type}" for pet_name, pet_type in show_me_pet_list)
    return vertical_list

    # Si no se encuentra ficha
    print("This member number doesn't exist or has a typo.")


# Función para agregar nueva ficha
def set_pet_card(pet_card):
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
