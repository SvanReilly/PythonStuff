# Alejandro Ortega Maldonado
subjects = [ "Filosofía", "Matemáticas", "Física", "Química", "Historia", "Lengua"]
calification = []
for subject in subjects:
    nota = float(input(f"Ingrese la nota de {subject}: "))
    if nota < 5:
        calification.append(subject)

print("Debes repetir las siguientes asignaturas:", ", ".join(calification))
