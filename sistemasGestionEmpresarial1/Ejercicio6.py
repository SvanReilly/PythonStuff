# Alejandro Ortega Maldonado

import turtle

ventana = turtle.Screen()
tortuga = turtle.Turtle()

def figura(lados):
    for _ in range(lados):
        tortuga.forward(100)
        tortuga.left(360 / lados)

lados = int(input("Introduzca el número de lados de la figura: "))
figura(lados)

ventana.exitonclick()
