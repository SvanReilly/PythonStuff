


#Escribe un programa que le pida al usuario su nombre y luego lo salude.
print("Por favor, escriba su nombre")
nombre = str(input())
print("Un saludo " + nombre + ". Le deseo un buen dia.")
#Escribe un programa que calcule la suma de dos números.
print("Escriba el primer sumando")
numero1= float(input())
print("Escriba el segundo sumando")
numero2=float(input())
resultado= numero1 + numero2

print("El resultado de la suma de " + str(numero1) + " y " + str(numero2) + " es: " + resultado)

#Escribe un programa que determine si un número es par o impar.
print("Escriba un numero a analizar: ")
numeroParImpar= int(input())

if numeroParImpar%2==0:
    print("El numero insertado es par")
elif numeroParImpar==0:
    print("El numero insertado es 0")
else:
    print("El numero insertado es impar")
#Escribe un programa que lea dos números y determine cuál es el mayor.


firstNumber = float(input())  # casteando una lectura de teclado
secondNumber= float(input())

if firstNumber>secondNumber:
    print(str(firstNumber) + " es mayor que " + str(secondNumber))
elif firstNumber<secondNumber:
    print(str(firstNumber) + " es menor que " + str(secondNumber))
else:
    print("El numero insertado es negativo")
