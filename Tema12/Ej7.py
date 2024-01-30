# Alejandro Ortega Maldonado
subjects = ["Física", "Filosofía", "Matemáticas",  "Historia", "Lengua"]
calification = []
for subject in subjects:
    nota = float(input(f"Ingrese la nota de {subject}: "))
    calification.append((subject, nota))

for subject, calification in calification:
    print(f"En {subject} has sacado {calification}.")
