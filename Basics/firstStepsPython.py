'''
comentario en bloque
'''
# comentario en linea
# and or not
#lectura = input()

booleano1 = False
booleano = True
# casting
# str ()
# bool()
# float()
# int()
print("Buenos días, tardes o noches. Por favor escriba su nombre")
nombre = str(input())

print("Ahora " + nombre +  ", inserte un numero entero")
numero_entero = int(input())  # casteando una lectura de teclado


if numero_entero>0:
    print("El numero insertado es positivo")
elif numero_entero==0:
    print("El numero insertado es 0")
else:
    print("El numero insertado es negativo")
