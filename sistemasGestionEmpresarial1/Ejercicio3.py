# Alejandro Ortega Maldonado

deportes = ["Fútbol", "Baloncesto", "Equitacion", "Natación", "Fútbol Sala"]

for deporte in deportes:
    if deporte.startswith("F"):
        continue
    elif deporte == "Equitacion":
        break
    else:
        print(deporte)
