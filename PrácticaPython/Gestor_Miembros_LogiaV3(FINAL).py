from math import sqrt
from time import sleep
from colorama import Fore
'''
print(Fore.CYAN + "Testing colors commands" + Fore.RESET)
print(Fore.LIGHTCYAN_EX + "Testing colors commands" + Fore.RESET)
print(Fore.RED + "Testing colors commands" + Fore.RESET)
print(Fore.LIGHTRED_EX + "Testing colors commands" + Fore.RESET)
print(Fore.YELLOW + "Testing colors commands" + Fore.RESET)
print(Fore.LIGHTYELLOW_EX + "Testing colors commands" + Fore.RESET)
print(Fore.MAGENTA + "Testing colors commands" + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Testing colors commands" + Fore.RESET)
print(Fore.BLUE + "Testing colors commands" + Fore.RESET)
print(Fore.LIGHTBLUE_EX + "Testing colors commands" + Fore.RESET)
print(Fore.BLACK + "Testing colors commands" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "Testing colors commands" + Fore.RESET)
print(Fore.WHITE + "Testing colors commands" + Fore.RESET)
print(Fore.LIGHTWHITE_EX + "Testing colors commands" + Fore.RESET)

boff = str(input("PAUSE"))
'''
continueButton = " "
usuarios = []
nombres_registrados = []


# Funcion seleccionarUsuario, mediante un for recorremos el array para comprobar si existe el usuario de nombre name, si existe devolverá dicho usuario
# En caso contrario seleccionará por defecto al usuario con posicion 0 en el array de usuarios, en este caso, al Administrador si existiese.

def seleccionarUsuario(name):

    for usuario in usuarios:
        if usuario["Nombre"] == name:
            usuarioactual = usuario
            break

        elif usuarios[0]["Nombre"] == name:
            usuarioactual = usuarios[0]

        else:

            usuarioactual = None


    return usuarioactual

# Establecer los permisos del antiguo maestre en False y los del nuevo maestre en True (aparentemente hecho)
def cambiarGranMaestre(name):
    granmaestre = usuarios[0]
    iniciado_registrado = False
    mensaje = ""

    for usuario in usuarios:
        if usuario["Nombre"] == name:
            granmaestre["Permisos"] = False
            usuario["Permisos"] = True
            granmaestre = usuario
            usuarios.remove(granmaestre)
            usuarios.insert(0, granmaestre)
            mensaje = Fore.LIGHTBLUE_EX + "DEMIURGO : El iniciado de nombre " + Fore.LIGHTYELLOW_EX + name + Fore.RESET + Fore.LIGHTBLUE_EX + " ha sido elegido como el nuevo Gran Maestre\n¿Signo de bonanza o desventura... *cof, cof*?" + Fore.RESET
            iniciado_registrado = True
            break
        if not iniciado_registrado:
            mensaje = Fore.LIGHTBLUE_EX + "DEMIURGO : Ese iniciado no existe, por lo tanto, El Gran Maestre " + Fore.RESET + Fore.LIGHTMAGENTA_EX + granmaestre["Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + " sigue regentando la logia." + Fore.RESET

    return mensaje


# Funcion para calcular el IMC
def calcularIMC(name):

    usuarioactual = seleccionarUsuario(name)

    height = float(usuarioactual["Peso"])
    weight = float(usuarioactual["Altura"])
    IMC = round(weight / (height ** 2), 1)

    return IMC


# Funcion Comprobar mayoria de edad del administrador, recorremos el array para comprobar si existe el administrador, si es el caso
# hara una comprobacion de edad y devolvera si es o no mayor de edad en base a una estructura if else, en caso de que no exista
# lo indicara con un print.
def granMaestreEdadChecker():
    granmaestre = usuarios[0]

    if granmaestre["Edad"] >= 18:
        mensaje = Fore.LIGHTBLUE_EX + "DEMIURGO : El Gran Maestre " + Fore.RESET + Fore.LIGHTMAGENTA_EX + granmaestre["Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + " es un adulto hecho y derecho.\nSobre sus hombros carga el hado de aquí nuestro menester..." + Fore.RESET
    else:
        mensaje = Fore.LIGHTBLUE_EX + "DEMIURGO : El Gran Maestre " + Fore.RESET + Fore.LIGHTMAGENTA_EX + granmaestre["Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + "es menor de edad.\nPara la sabiduría no existe el tiempo..." + Fore.RESET

    return mensaje


# Funcion agregarUsuario, mediante un for recorremos el array para saber si antes de nada existe el usuario administrador
# en cuyo caso no exista, se generará uno con parámetros establecidos y se almacenará en el array de usuarios en la primera posición.
# En caso contrario

def agregarUsuario(name, height, weight, age):
    if name in nombres_registrados:
        mensaje = Fore.LIGHTBLUE_EX + "DEMIURGO: El iniciado de apodo " + Fore.RESET + Fore.LIGHTYELLOW_EX + name + Fore.RESET + Fore.LIGHTBLUE_EX + " ya forma parte de nuestro gremio. Pruebe otro alias." + Fore.RESET
    else:
        nombres_registrados.append(name)
        if len(usuarios) > 0:
            primer_usuario = usuarios[0]
            if primer_usuario["Nombre"] == name:
                mensaje = Fore.LIGHTBLUE_EX + "DEMIURGO: El iniciado de apodo " + Fore.RESET + Fore.LIGHTYELLOW_EX + name + Fore.RESET + Fore.LIGHTBLUE_EX + " ya forma parte de nuestro gremio. Pruebe otro alias." + Fore.RESET
            else:
                usuario = {
                    "Nombre": str(name),
                    "Altura": sqrt(float(height)**2),
                    "Peso": sqrt(float(weight)**2),
                    "Edad": sqrt(int(age)**2),
                    "Password": 1234,
                    "Permisos": False
                }
                usuarios.append(usuario)
                mensaje = Fore.LIGHTBLUE_EX + "DEMIURGO: Iniciado abducido con éxito." + Fore.RESET
        else:
            usuario = {
                "Nombre": str(name),
                "Altura": sqrt(float(height) ** 2),
                "Peso": sqrt(float(weight) ** 2),
                "Edad": sqrt(int(age) ** 2),
                "Password": 1234,
                "Permisos": True
            }
            usuarios.append(usuario)
            mensaje = "El Gran Maestre de la Orden 'spawneó' con éxito en el sistema."

    return "\n" + mensaje + "\n"


def listarUsuariosSistema():
    usuarios_sistema = []
    for usuario in usuarios:
        usuarios_sistema.append(usuario["Nombre"])

    listado_vertical = "\n".join(usuarios_sistema)
    return listado_vertical


def datosIniciado(name):
    for usuario in usuarios:
        if usuario["Nombre"] == name:
            recopilarIniciado = usuario
            break
        else:
            recopilarIniciado = None

    return recopilarIniciado


stayCurious = True

print(Fore.GREEN + "\nBIENVENIDO AL GESTOR DE INICIADOS PITAGÓRICOS DE LA ORDEN DE MOUNTIME:" + Fore.RESET)
sleep(0.5)
print(Fore.RED + "   0% : ..." + Fore.RESET)
sleep(1.5)
print(Fore.RED + "  11%" + Fore.RESET + Fore.LIGHTRED_EX + " : INICIALIZANDO SISTEMA ORBITAL CENTRALIZADO DE COMANDOS Y BUCLES." + Fore.RESET)
sleep(1.5)
print(Fore.RED + "  23%" + Fore.RESET + Fore.LIGHTMAGENTA_EX + " : COTEJANDO ID DE LA HERMANDAD PITAGóRICA." + Fore.RESET)
sleep(1.5)
print(Fore.RED + "  45%" + Fore.RESET + Fore.MAGENTA + " : COMPROBANDO AFORO MÁXIMO DEL ÁGORA VIRTUAL." + Fore.RESET)
sleep(1.5)
print(Fore.RED + "  67%" + Fore.RESET + Fore.CYAN + " : INSERTANDO UNA TRETAKTYS DE MALA CALIDAD." + Fore.RESET)
sleep(1.5)
print(Fore.RED + "  84%" + Fore.RESET + Fore.LIGHTBLUE_EX + " : RENDERIZANDO POCA COSA, LA VERDAD." + Fore.RESET)
sleep(1.5)
print(Fore.RED + "  94%" + Fore.RESET + Fore.LIGHTCYAN_EX + " : INTERPRETANDO INSTRUCCIONES DEL CATETO REDUNDANTE." + Fore.RESET)
sleep(1.5)
print(Fore.LIGHTGREEN_EX + " 100%" + Fore.RESET + Fore.LIGHTGREEN_EX + " : MATERIALIZANDO SISTEMA GESTOR BASADO EN ARITMÉTICA BÁSICA." + Fore.RESET)
sleep(5)
print(Fore.LIGHTBLACK_EX + "\nPara configurar el sistema siga las siguientes instrucciones:\n" + Fore.RESET)
sleep(1)

baited = str(input("Inserte el nombre del Gran Maestre de la Orden: "))
print(Fore.LIGHTBLUE_EX + "\nDEMIURGO : ¿Cómo...? ¿Cómo dices...?" + Fore.RESET)

continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

print(Fore.LIGHTBLUE_EX +Fore.LIGHTBLUE_EX + "DEMIURGO : ¿De verdad pensaste que...?"+ Fore.RESET)

continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

print(Fore.LIGHTBLUE_EX +Fore.LIGHTBLUE_EX + "DEMIURGO : JAJAJAJA ya decido yo por tí, joven... Toma asiento. >:3"+ Fore.RESET)

name = "Svan Sidis Reilly"

continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

print(Fore.LIGHTBLUE_EX + "DEMIURGO : Sí, sí... Su nombre es... " + Fore.LIGHTMAGENTA_EX + name + Fore.RESET + Fore.LIGHTBLUE_EX + ". El creador de MounTime Project\ny su simulación 'El Brillo de los Gigantes' (*`.´*)." + Fore.RESET)

continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

print(Fore.LIGHTBLUE_EX + "DEMIURGO : Su peso en ayunas era... sí, este. No está en mala forma física,\ntiene un metabolismo y ritmo circadiano envidiable *cof, cof*" + Fore.RESET)

weight = 75.2

continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

print(Fore.LIGHTBLUE_EX + "DEMIURGO : El Gran Maestre no es para nada bajo aunque tampoco es el más alto de la Sala Suma, sin embargo,"
    "\nsu creatividad es inconmensurable. Hmm... " + Fore.RESET)

height = 1.82

continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

print(Fore.LIGHTBLUE_EX + "DEMIURGO : Aparenta menos edad de la que tiene o eso dicen los mortales con los que frecuenta, "
    + "\n" + "pero la forma material es imperfecta y mi visión eidética ve a través de su alma... " + Fore.RESET)

age = 28

print(Fore.WHITE + "\n*Materializando Gran Maestre... Espere, por favor.*" + Fore.RESET)

sleep(2)

mensaje = agregarUsuario(name, weight, height, age)

print(mensaje)

continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

usuarioactual = seleccionarUsuario(name)

print("El iniciado actual es " + Fore.LIGHTYELLOW_EX + usuarioactual["Nombre"] + Fore.RESET + "\n")

while stayCurious:

    print(Fore.WHITE + "*Accedes a la Sala Suma del Consejo Primordial de MounTime Project*"
          + "\n______________________________________________________________________"
          + "\n"
          + Fore.LIGHTWHITE_EX + "1. Saludo masónico."
          + "\n"
          + Fore.LIGHTCYAN_EX + "2. Calcular IMC"
          + "\n"
          + Fore.MAGENTA + "3. Comprobar mayoria de edad"
          + "\n"
          + Fore.LIGHTMAGENTA_EX + "4. Listar nombres de iniciados registrados en la logia"
          + "\n"
          + Fore.BLUE + "5. Añadir nuevo iniciado"
          + "\n"
          + Fore.LIGHTBLUE_EX + "6. Datos del iniciado"
          + "\n"
          + Fore.YELLOW + "7. Cambiar de usuario."
          + "\n"
          + Fore.LIGHTRED_EX + "8. Nombrar un nuevo Gran Maestre. (" + Fore.RESET + Fore.LIGHTBLUE_EX + "DEMIURGO: " + Fore.RESET + Fore.LIGHTRED_EX + "SÓLO EL GRAN MAESTRE SE ATREVERÍA A CEDER TITÁNICA DESVENTURA A OTRO MORTAL.)" + Fore.RESET
          + "\n"
          + Fore.WHITE + "9. Salir."
          + "\n______________________________________________________________________")
    sleep(0.5)
    numMenu = str(input("Inserte un numero del 1 al 9 (preferiblemente...): " + Fore.RESET))

    if numMenu == "1":
        print(Fore.WHITE + "\n*El miembro actual muestra la marca de la estrella de 6 puntas y, a continuación, alguien se acerca estrechando su mano siguiendo el protocolo masónico.*\n" + Fore.RESET)
        sleep(3)
        if usuarioactual != usuarios[0]:
            print(Fore.LIGHTBLUE_EX + "DEMIURGO : Bienvenido, " + Fore.RESET + Fore.LIGHTYELLOW_EX + usuarioactual["Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + " ¿Qué tal va todo en el mundo material?" + Fore.RESET)
        else:
            print(Fore.LIGHTBLUE_EX + "DEMIURGO : " + Fore.WHITE + "*Sonríe* " + Fore.RESET + Fore.LIGHTBLUE_EX + "Bienvenido mi viejo amigo, " + Fore.RESET + Fore.LIGHTMAGENTA_EX + usuarioactual["Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + " ¿Cómo va esa simulación de espacios no euclidianos en Unreal Engine 5?" + Fore.RESET)
        continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

    elif numMenu == "2":
        mensaje2 = Fore.LIGHTBLUE_EX + "DEMIURGO : El IMC del iniciado seleccionado es de: "
        name = usuarioactual["Nombre"]
        IMC = calcularIMC(name)
        if IMC < 16:
            mensaje2 += str(IMC) + Fore.BLUE + " (Delgadez severa.)" + Fore.RESET
        elif 16 <= IMC < 17:
            mensaje2 += str(IMC) + Fore.LIGHTBLUE_EX + " (Delgadez moderada.)" + Fore.RESET
        elif 17 <= IMC < 18.5:
            mensaje2 += str(IMC) + Fore.GREEN + " (Delgadez aceptable.)" + Fore.RESET
        elif 18.5 <= IMC < 25:
            mensaje2 += str(IMC) + Fore.LIGHTGREEN_EX + " (Normopeso.)" + Fore.RESET
        elif 25 <= IMC < 30:
            mensaje2 += str(IMC) + Fore.MAGENTA + " (Sobrepeso.)" + Fore.RESET
        elif 30 <= IMC < 35:
            mensaje2 += str(IMC) + Fore.LIGHTMAGENTA_EX + " (Obesidad de Tipo 1.)" + Fore.RESET
        elif 35 <= IMC < 40:
            mensaje2 += str(IMC) + Fore.RED + " (Obesidad de Tipo 2.)" + Fore.RESET
        elif 40 <= IMC < 50:
            mensaje2 += str(IMC) + Fore.RED + " (Obesidad de Tipo 3: Mórbida.)" + Fore.RESET
        else:
            mensaje2 += str(IMC) + Fore.LIGHTRED_EX + " (Obesidad de Tipo 4: EXTREMA.)" + Fore.RESET
        print(mensaje2 + Fore.RESET)
        continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

    elif numMenu == "3":
        mensaje3 = granMaestreEdadChecker()
        print(mensaje3)
        continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

    elif numMenu == "4":
        lista_usuarios = listarUsuariosSistema()
        print(Fore.LIGHTBLUE_EX + "\nDEMIURGO : Aquí tienes una previa de la lista solicitada.\n" + Fore.RESET + Fore.LIGHTRED_EX + "\nComienzo de la lista de miembros:" + Fore.RESET)
        print(lista_usuarios)
        print(Fore.LIGHTRED_EX + "Fin de la lista de miembros.\n" + Fore.RESET)
        continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

    elif numMenu == "5":
        name = str(input(Fore.LIGHTBLUE_EX + "DEMIURGO : Inserte un nuevo nombre de iniciado: " + Fore.RESET))
        weight = float(input(Fore.LIGHTBLUE_EX + "DEMIURGO : Inserte el peso del nuevo iniciado: " + Fore.RESET))
        height = float(input(Fore.LIGHTBLUE_EX + "DEMIURGO : Inserte la altura del nuevo iniciado: " + Fore.RESET))
        age = float(input(Fore.LIGHTBLUE_EX + "DEMIURGO : Inserte la edad del nuevo iniciado: " + Fore.RESET))
        mensaje5 = agregarUsuario(name, weight, height, age)
        print(mensaje5)
        continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

    elif numMenu == "6":
        name = input(Fore.LIGHTBLUE_EX + "\nDEMIURGO : Inserte un nombre de un miembro para obtener su información\n" + Fore.RESET)
        datosRecopilados = datosIniciado(name)
        if datosRecopilados != None:
            mensaje6= Fore.LIGHTBLUE_EX + "DEMIURGO : Los datos del miembro solicitado son los siguientes: " + Fore.RESET
        else:
            mensaje6= Fore.LIGHTBLUE_EX + "DEMIURGO : El miembro no existe." + Fore.RESET
        print(mensaje6)
        print(datosRecopilados)
        continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

    # En seleccionarUsuario tengo que arreglar que cuando selecciono otro usuario actual y decido volver a elegir al
    # administrador me muestre un mensaje distinto al de no existe.
    elif numMenu == "7":
        print(Fore.LIGHTBLUE_EX + "\nDEMIURGO : ¿Desea cambiar de iniciado?" + Fore.RESET)
        name = input(Fore.LIGHTBLUE_EX + "DEMIURGO : Inserte el nombre de un iniciado registrado, por favor: " + Fore.RESET)
        usuarioactual = seleccionarUsuario(name)

        if usuarioactual is None:
            mensaje7 = Fore.LIGHTBLUE_EX + "DEMIURGO : Ese iniciado no existe, así que El Gran Maestre " + Fore.RESET + Fore.LIGHTMAGENTA_EX + usuarios[0][
                "Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + " ha vuelto a la tribuna." + Fore.RESET

        elif usuarioactual != usuarios[0]:
            mensaje7 = Fore.LIGHTBLUE_EX + "DEMIURGO : El iniciado actual es " + Fore.RESET + Fore.LIGHTYELLOW_EX + usuarioactual["Nombre"] + Fore.RESET

        else:

            mensaje7 = Fore.LIGHTBLUE_EX + "DEMIURGO : Se ha invocado al Gran Maestre " + Fore.RESET + Fore.LIGHTMAGENTA_EX + usuarioactual["Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + " de nuevo a la tribuna." + Fore.RESET

        print(mensaje7)

        continueButton = str(input("\n- Pulse ENTER para continuar -\n"))
    elif numMenu == "8":
        granmaestre = usuarios[0]

        if usuarioactual == granmaestre:
            print(Fore.LIGHTBLUE_EX + "\nDEMIURGO : Gran Maestre " + Fore.RESET + Fore.LIGHTMAGENTA_EX + granmaestre["Nombre"] + Fore.RESET + Fore.LIGHTBLUE_EX + " ¿Desea ceder su rango... *cof, cof*?" + Fore.RESET)
            sleep(2)
            name = input(Fore.LIGHTBLUE_EX + "DEMIURGO : Escriba el nombre del (des)afortunado... " + Fore.RESET)
            cambiarGranMaestre(name)
            mensaje = cambiarGranMaestre(name)
            print("\n" + mensaje)
            continueButton = str(input("\n- Pulse ENTER para continuar -\n"))
        else:
            print(Fore.LIGHTBLUE_EX + "DEMIURGO : Sólo el Gran Maestre " + Fore.RESET + Fore.LIGHTMAGENTA_EX + granmaestre[
                "Nombre"] + Fore.RESET + " está autorizado para decidir el futuro de la logia." + Fore.RESET)
            continueButton = str(input("\n- Pulse ENTER para continuar -\n"))

    else:
        print("\nEJECUTANDO PROTOCOLO DE DESPEDIDA DE LA LOGIA: " + Fore.LIGHTRED_EX + "\n 0%" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTRED_EX + "18%" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTRED_EX + "34%" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTRED_EX + "55%" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTRED_EX + "73%" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTRED_EX + "86%" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTRED_EX + "94%" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTMAGENTA_EX + "\n*Simposio masónico: Finalizado con éxito.*" + Fore.RESET)
        sleep(0.25)
        print(Fore.LIGHTBLUE_EX + "\nDEMIURGO : Tenga un buen día, iniciado/a." + Fore.RESET)
        sleep(3)
        stayCurious = False
