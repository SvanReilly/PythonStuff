# Alejandro Ortega Maldonado

x = 0
while x < 20:
    if x % 2 == 0:
        print(f"{x} es par")
        x += 1
        continue
    elif x == 15:
        break
    else:
        print(x)
        x += 1
