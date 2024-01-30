# Miguel Ángel Roldán de Haro
age = int(input("Ingrese su edad: "))
earnings = float(input("Ingrese su sueldo mensual: "))
if age > 16 and earnings >= 1000:
    print("Debe tributar.")
else:
    print("No debe tributar.")
