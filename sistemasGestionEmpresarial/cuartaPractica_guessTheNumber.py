import random

playAgain = True
randomNumber = int(random.randint(1, 50))
print(randomNumber)

while playAgain:
    numberIns = int(input("Para resolver este puzzle tienes que adivinar el número"
                          "\nen el que estoy pensando. Ojo, porque solo tienes 5 intentos."
                          "\nEl número se encuentra entre el 0 y el 50:"
                          "\n"))
    counter = 1
    while counter < 5:

        if numberIns > randomNumber:
            numberIns = int(input(f"El número que buscas es MENOR que {numberIns}: "))
            counter = counter + 1
        elif numberIns < randomNumber:
            numberIns = int(input(f"El número que buscas es MAYOR que {numberIns}: "))
            counter = counter + 1
        elif numberIns == randomNumber and counter <= 5:
            print(f"¡Has acertado! El número correcto era: {randomNumber}")
            counter = 6

    if numberIns != randomNumber and counter == 5:
        print(f"\n¡Ahh estuviste cerca! El número correcto era: {randomNumber}")

    playAgainSTR = str(input("\n¿Quieres seguir jugando? (S/N): "))
    if playAgainSTR.__eq__("S" or "s" or "si" or "Sí" or "sí" or "yes"):
        playAgain
    elif playAgainSTR.__eq__("hell yeah!"):
        print("\nYEEEAAAH WE TALKING ABOUT IT MATE!!! >:D\n")
        playAgain
    else:
        playAgain = False
