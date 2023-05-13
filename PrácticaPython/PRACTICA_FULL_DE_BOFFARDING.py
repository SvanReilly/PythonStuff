from time import sleep

usuarios = []


# Funcion seleccionarUsuario, mediante un for recorremos el array para comprobar si existe el usuario de nombre name, si existe devolverá dicho usuario
# En caso contrario seleccionará por defecto al usuario con posicion 0 en el array de usuarios, en este caso, al Administrador si existiese.

def seleccionarUsuario(name):
    usuarioactual = usuarios[0]
    for usuario in usuarios:
        if usuario["Nombre"] == name:
            usuarioactual = usuario
        else:
            print("Ese iniciado no existe, así que El Gran Maestre " + usuarioactual[
                "Nombre"] + " ha vuelto a la tribuna.")
    return usuarioactual


def cambiarGranMaestre(name):
    granmaestre = usuarios[0]
    mensaje = ""

    for usuario in usuarios:
        if usuario["Nombre"] != name:
            mensaje = "Ese iniciado no existe, por lo tanto, El Gran Maestre " + granmaestre[
                "Nombre"] + " sigue regentando la logia."
        else:
            granmaestre = usuario
            usuarios.remove(granmaestre)
            usuarios.insert(0, granmaestre)
            mensaje = "El iniciado de nombre " + name + " ha sido elegido como el nuevo Gran Maestre ¿Signo de bonanza o desventura... *cof, cof*?"

    return mensaje


# Funcion para calcular el IMC
def calcularIMC(name):
    usuarioactual = seleccionarUsuario(name)

    height = float(usuarioactual["Peso"])
    weight = float(usuarioactual["Altura"])
    IMC = int(weight / (height ** 2))

    return str(IMC)


# Funcion Comprobar mayoria de edad del administrador, recorremos el array para comprobar si existe el administrador, si es el caso
# hara una comprobacion de edad y devolvera si es o no mayor de edad en base a una estructura if else, en caso de que no exista
# lo indicara con un print.
def granMaestreEdadChecker():
    granmaestre = usuarios[0]

    if granmaestre["Edad"] >= 18:
        mensaje = "El Gran Maestre de la orden es un adulto hecho y derecho. Sobre sus hombros carga el hado de aquí nuestro menester..."
    else:
        mensaje = "El Gran Maestre de la Orden es menor de edad. Para la sabiduría no existe el tiempo..."

    return mensaje


# Funcion agregarUsuario, mediante un for recorremos el array para saber si antes de nada existe el usuario administrador
# en cuyo caso no exista, se generará uno con parámetros establecidos y se almacenará en el array de usuarios en la primera posición.
# En caso contrario
def agregarUsuario(name, height, weight, age):
    if len(usuarios) > 0:
        primer_usuario = usuarios[0]
        if primer_usuario["Nombre"] == name:
            mensaje = "El iniciado de apodo " + name + " ya forma parte de nuestro gremio. Pruebe otro alias."
        else:
            usuario = {
                "Nombre": str(name),
                "Altura": float(height),
                "Peso": float(weight),
                "Edad": int(age),
                "Password": 1234,
                "Permisos": False
            }
            usuarios.append(usuario)
            mensaje = "Iniciado abducido con éxito."
    else:
        usuario = {
            "Nombre": str(name),
            "Altura": float(height),
            "Peso": float(weight),
            "Edad": int(age),
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

    return usuarios_sistema


def datosIniciado(name):
    for usuario in usuarios:
        if usuario["Nombre"] == name:
            recopilarIniciado = usuario

        else:
            recopilarIniciado = None
            print("El iniciado no existe.")

    return recopilarIniciado


stayCurious = True

print("\nBienvenido al gestor de iniciados pitagóricos de la Orden de MounTime.")
sleep(0.5)
print("  0%")
sleep(1.5)
print(" 11% : INICIALIZANDO SISTEMA ORBITAL DE COMANDOS Y BUCLES.")
sleep(1.5)
print(" 23% : COTEJANDO ID DE LA HERMANDAD PITAGóRICA.")
sleep(1.5)
print(" 45% : COMPROBANDO AFORO MÁXIMO DEL ÁGORA VIRTUAL.")
sleep(1.5)
print(" 67% : INSERTANDO UNA TRETAKTYS DE MALA CALIDAD.")
sleep(1.5)
print(" 84% : RENDERIZANDO POCA COSA, LA VERDAD.")
sleep(1.5)
print(" 94% : INTERPRETANDO INSTRUCCIONES DEL CATETO REDUNDANTE.")
sleep(1.5)
print("100% : MATERIALIZANDO SISTEMA GESTOR BASADO EN ARITMÉTICA BÁSICA.")
sleep(5)
print("\nPara configurar el sistema siga las siguientes instrucciones:\n")
sleep(1)

print("Inserte el nombre del Gran Maestre de la Orden: ")
sleep(3)
print("DEMIURGO : ¿Cómo...? ¿Cómo dices...?")
sleep(3)
print("DEMIURGO : ¿De verdad pensaste que...?")
sleep(3)
print("DEMIURGO : JAJAJAJA ya decido yo por tí, joven... Toma asiento. >:3")


name = "Svån Sidis Reilly"


sleep(5)
print(
    "DEMIURGO : Sí, sí... su nombre es... " + name + ". El creador de MounTime Project y su simulación 'El Brillo de los Gigantes' (*`.´*).")
sleep(6)
print(
    "DEMIURGO : Su peso en ayunas era... sí, este. No está en mala forma física, tiene un metabolismo y ritmo circadiano envidiable *cof, cof*")


weight = 75.2


sleep(6)
print(
    "DEMIURGO : El Gran Maestre no es bajo aunque tampoco es el más alto de la Sala Suma, sin embargo, su creatividad es inconmensurable. Hmm... ")

height = 1.82

sleep(6)
print(
    "DEMIURGO : Aparenta menos edad de la que tiene o eso dicen los mortales con los que frecuenta pero la forma material es imperfecta y mi visión eidética ve a través de su alma... ")


age = 28

sleep(8)

mensaje = agregarUsuario(name, weight, height, age)
print(mensaje)
usuarioactual = seleccionarUsuario(name)
sleep(3)

while stayCurious:

    print("\n*Accedes a la Sala Suma del Consejo Primordial de MounTime Project*\n"
          + "1. Saludo masónico."
          + "\n"
          + "2. Calcular IMC"
          + "\n"
          + "3. Comprobar mayoria de edad"
          + "\n"
          + "4. Listar nombres de iniciados registrados en la logia"
          + "\n"
          + "5. Añadir nuevo iniciado"
          + "\n"
          + "6. Datos del iniciado"
          + "\n"
          + "7. Cambiar de usuario."
          + "\n"
          + "8. Nombrar un nuevo Gran Maestre (DEMIURGO: SÓLO EL GRAN MAESTRE SE ATREVERÍA A CEDER TITÁNICA DESVENTURA A OTRO MORTAL.)"
          + "\n"
          + "Si usted desea abandonar la reunión inserte cualquier valor o carácter no incluido en el menú")

    numMenu = str(input("\nInserte un numero del 1 al 8 (preferiblemente...): \n"))

    if numMenu == "1":
        print("*Estrechan su mano siguiendo el protocolo*"
              + "\nDEMIURGO : Bienvenido, " + usuarioactual["Nombre"] + " ¿Qué tal va todo en el mundo material?")
        sleep(5)

    elif numMenu == "2":
        IMC = calcularIMC(usuarioactual)
        print("El IMC del iniciado seleccionado es de: " + IMC)
        sleep(4)

    elif numMenu == "3":
        mensaje = granMaestreEdadChecker()
        print(mensaje)
        sleep(6)

    elif numMenu == "4":
        lista_usuarios = listarUsuariosSistema()
        print("\nComienzo de la lista de iniciados:\n")
        print(lista_usuarios)
        print("\nFin de la lista de iniciados.\n")
        sleep(8)

    elif numMenu == "5":
        name = str(input("Inserte un nuevo nombre de iniciado: "))
        weight = float(input("Inserte el peso del nuevo iniciado: "))
        height = float(input("Inserte la altura del nuevo iniciado: "))
        age = float(input("Inserte la edad del nuevo iniciado: "))
        mensaje = agregarUsuario(name, weight, height, age)
        print(mensaje)
        sleep(4)

    elif numMenu == "6":
        name = input("\nInserte un nombre de usuario para obtener su información\n")
        mensaje = datosIniciado(name)
        print(mensaje)
        sleep(4)

    elif numMenu == "7":
        print("\n¿Desea cambiar de iniciado?")
        name = str(input("Inserte un nombre de un iniciado registrado, por favor: "))
        usuarioactual = seleccionarUsuario(name)
        print("El iniciado actual es " + usuarioactual["Nombre"])
        sleep(4)
    elif numMenu == "8":
        granmaestre = usuarios[0]

        if usuarioactual == granmaestre:
            print("\nGran Maestre " + granmaestre["Nombre"] + " ¿Desea ceder su rango... *cof, cof*?")
            sleep(2)
            name = input("Escriba el nombre del (des)afortunado... ")
            cambiarGranMaestre(name)
            mensaje = cambiarGranMaestre(name)
            print("\n" + mensaje)
            sleep(7)
        else:
            print("Sólo el Gran Maestre " + granmaestre[
                "Nombre"] + " está autorizado para decidir el futuro de la logia.")
            sleep(8)

    else:
        print("\nEJECUTANDO PROTOCOLO DE DESPEDIDA DE LA LOGIA: 0%")
        sleep(0.25)
        print("18%")
        sleep(0.25)
        print("34%")
        sleep(0.25)
        print("55%")
        sleep(0.25)
        print("73%")
        sleep(0.25)
        print("86%")
        sleep(0.25)
        print("94%")
        sleep(0.25)
        print("* Simposio masónico: Finalizado*")
        sleep(0.25)
        print("\nDEMIURGO : Tenga un buen día, iniciado/a.")
        sleep(3)
        stayCurious = False
