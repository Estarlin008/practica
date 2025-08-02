from sys import prefix
def Convertil():
    euro = float (input("ingrese la cantida de euro"))
    tasaCambio = 67.17
    cambio = euro * tasaCambio
    print(f"{cambio:.2f}")

def MillasPies():
    millas = int (input("ingrese las millas"))
    pies = 5280
    print(millas * pies)

def DeterminarEdad():
    AA = int (input("ingrese el año actual"))
    AN = int (input("ingrese el año de nacimiento"))
    if AA > AN:
        print("la edad es:" + str(AA - AN))
    else:
        print("ingrese un año actual valido")

def ConvertilFa():
    C = int (input("ingrese la temperatura en Celsius"))
    print((C * 9/5)+32)

def ITBIS():
    cantidad = int(input("ingrese la cantidad del producto"))
    precioUni = int(input("ingrese le precio unitario del producto"))
    subTotal = cantidad * precioUni
    itbis = subTotal * 0.18
    totalPagar = subTotal + itbis
    print(itbis)
    print(totalPagar)

def numeroPar():
    numero = int (input("ingrese el numero"))
    z = numero % 2
    if z == 0:
        print("numero par:" + str(numero))
    else:
        print("numero impar" + str(numero))

def NumeroPrimo():
    numero = int (input("ongrese el numero"))
    divisible = False
    for i in range(2,numero):
        if numero % i == 0:
            divisible = True
            break
    if divisible:
        print(f"{numero} no es primo")
    else:
        print(f"{numero} es primo")

def anoBiciesto():
    ano = int(input("ingrese el año"))
    if ano % 4 == 0 and ano % 100 == 0:
        print(f"{ano} no es biciesto")

    if ano % 4 == 0 and ano % 400 == 0:
        print(f"{ano} no es biciesto")

    if ano % 4 == 0:
        print(f"{ano} si es biciesto")

def ConocerEdadAnoBiciesto():
    AA = int(input("ingrese el año actual"))
    AN = int(input("ingrese el año de nacimiento"))

    if AA > AN:
        if AN % 2 != 0:
            print(f"la edad es:" + str(AA - AN))
        else:
            print("ERROR")
    else:
        print("ingrese un año aceptable")

def numeroParRango():
    PrimerRango = int(input("ingrese el primer numero"))
    SegundoRango = int(input("ingrese el segundo numero"))

    if SegundoRango > PrimerRango:
        for i in range(PrimerRango,SegundoRango):
            if i % 2 == 0:
                print(i)
    else:
        print("ingrese un segundo numero mayor al primero")

def añosbiciestoRango():
    ano1 = int(input("ingrese el primer año"))
    ano2 = int(input("ingrese el segundo año"))

    if ano2 > ano1:
        for i in range(ano1,ano2,1):

            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                print(f"{i} si es biciesto")

    else:
        print("ingrese eun numero mayor al primero")
        
def perro():
    str ladra = int(input("ingrese el sonido del perro"))
    if ladra == "guau":
        print("el perro ladra")
    else:
        print("el perro no ladra")

def mas():
    e = int(input("ingrese el primer numero"))
    f = int(input("ingrese el segundo numero"))
    print("la suma es:" + str(e + f))
    
def Mascota():
    malo = input("es malo")
    bueno = input("eres bueno")
    if malo == "si":
        print("el perro es malo")
    elif bueno == "si":
        print("el perro es bueno")

def MostrarMenu():
    print("------------MENU------------")
    print("1:Convertil de peso a euro")
    print("2:Convertil de millas a pies")
    print("3:Determinar la edad de una persona")
    print("4:Convertil de Celsius a Fahrenheit")
    print("5:Determinar el ITBIs")
    print("6:Determinar si un numero es par")
    print("7:Determinar si un numero es primo")
    print("8:Determinar si un año es biciesto")
    print("9:Determinar si la edad de una persona si el año de nacimiento es impar")
    print("10:Los numero pares dentro de un rango")
    print("11:los años biciestos dentro de un rango")
    print("12:ladra")
    print("13:salir")

while True:
    MostrarMenu()
    opcion = int(input("seleciones una de las opciones"))

    match opcion:
        case 1:
            Convertil()
        case 2:
            MillasPies()
        case 3:
            DeterminarEdad()
        case 4:
            ConvertilFa()
        case 5:
            ITBIS()
        case 6:
            numeroPar()
        case 7:
            NumeroPrimo()
        case 8:
            anoBiciesto()
        case 9:
            ConocerEdadAnoBiciesto()
        case 10:
            numeroParRango()
        case 11:
            añosbiciestoRango()
        case 12:
            perro()
        case 13:
            print("hasta luego👋😄")
            break
