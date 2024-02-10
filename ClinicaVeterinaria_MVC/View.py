# Alejandro Ortega Maldonado

from Controller import new_card, print_cards, get_pet_card
from colorama import *

database_name = "your_database_name"
user = "admin"
password = "1234"
host = "localhost"  # Puede ser localhost si la base de datos está en tu máquina
port = "5432"  # El puerto predeterminado para PostgreSQL es 5432


def main():
    system = True
    while system:
        print(Fore.CYAN + "Vet" + Fore.LIGHTCYAN_EX + "eri" + Fore.BLUE + "nary" + " "
              + Fore.LIGHTBLUE_EX + "Cli" + Fore.LIGHTGREEN_EX + "nic" + Fore.RESET)
        print("__________________________________________")
        print(Fore.LIGHTGREEN_EX + "|        1. Insert New Pet Card          |" + Fore.RESET)
        print(Fore.MAGENTA + "|        2. List Every Pet Card          |" + Fore.RESET)
        print(Fore.YELLOW + "|        3. Search by Member Nº          |" + Fore.RESET)
        print("__________________________________________")
        option = input(Fore.RED + "Select an option" + Fore.RESET + " ("
                       + Fore.BLUE + "1" + ", "
                       + Fore.YELLOW + "2" + Fore.RESET + " or "
                       + Fore.GREEN + "3" + Fore.RESET + "): ")

        if option == '1':
            new_card()
        elif option == '2':
            member_pet_list = print_cards()
            print(Fore.YELLOW + "___________________" + Fore.RESET + "\n" + member_pet_list)
        elif option == '3':
            member_number = int(input("Insert a member number: "))
            member_pet_list = get_pet_card(member_number)
            print(Fore.YELLOW + "___________________" + Fore.RESET + "\n" + member_pet_list)
        else:
            print("Not a valid option")

        continue_input = input("Wish to make another request (y/n): ")

        if continue_input.lower() == 'n':
            print("Logging out...")
            print("_________________________________________")
            system = False

        elif continue_input.lower() != 'y':
            print("Invalid Entry. please 'y' or 'n'.")


if __name__ == "__main__":
    print()
    main()
