#1. Escribe un programa que le pida al usuario su nombre y luego lo salude.
print("Por favor, escriba su nombre a continuación: ")
nombre = str(input())
print("Le deseo un muy buen día, " + nombre + ".")

#2. Escribe un programa que calcule la suma de dos números.

print("Por favor, inserte el primer sumando: ")
sumando1 = float(input())
print("Por favor, inserte el primer sumando: ")
sumando2 = float(input())

resultado = float(sumando1 + sumando2)
print("El resultado de la suma entre " + str(sumando1) + " y " + str(sumando2) + " es " + str(resultado))

#3. Escribe un programa que determine si un número es par o impar.

print("Por favor, inserte un número a analizar distinto de 0: ")
numInsertado = int(input())

while numInsertado == 0:
    print("Un numero diferente de 0, humano.")
    numInsertado = int(input())

if numInsertado % 2 == 0:
    print("El numero insertado es par.")
else:
    print("El numero insertado es impar.")

#4. Escribe un programa que lea dos números y determine cuál es el mayor.

print("Por favor, inserte el primer numero a comparar: ")
numComparar1 = int(input())
print("Por favor, inserte el segundo numero a comparar: ")
numComparar2 = int(input())

if numComparar1 > numComparar2:
    print("El numero " + str(numComparar1) + " es mayor que " + str(numComparar2))
elif numComparar1 < numComparar2:
    print("El numero " + str(numComparar1) + " es menor que " + str(numComparar2))
else:
    print("Ambos numeros son iguales.")

print("Ha sido todo un placer, " + str(nombre) + ". Hasta pronto!")
