# Alejandro Ortega Maldonado

ageCheckerMessage = ""
ageTextBox = ""
correct = True


def ageChecker(age):
    if age >= 18.0:
        ageCheckerMessage = "Es mayor de edad."
    elif 0 <= age < 18.0:
        ageCheckerMessage = "Es menor de edad."
    else:
        ageCheckerMessage = "Introduzca un valor válido"

    return ageCheckerMessage


while correct:
    try:
        ageTextBox = float(input("Inserte una edad: "))
        correct = False
    except ValueError:
        print("Valores numericos unicamente.")

print(ageChecker(ageTextBox))
