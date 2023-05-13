"""
FOR
"""

for i in range (1,10):
    contador=0
    cadena="Hola Mundo"

for letra in cadena:
    if letra=="a":
        contador+=1
    cadena[letra]="A"
print("La cadena es: " + cadena)


"""
WHILE condicion:
"""

"""
ARRAYS
"""
ejemplo=[]
#Insertar
ejemplo.append("administrador")
ejemplo.append("Usuario1")

#ejemplo=["administrador", "Usuario1"]
#Mostrar
print(ejemplo[0])


"""
FUNCTIONS
"""

personas=[]

def agregar(name,surname):
    #Estructura clave-valor
    persona = {
        "nombre": name,
        "apellido": surname
    }
    personas.append(persona)
    print("Persona añadida con exito.")

agregar("Alejandro", "Ortega")
for p in personas:
    print(p["nombre"])
    print(p["apellido"])