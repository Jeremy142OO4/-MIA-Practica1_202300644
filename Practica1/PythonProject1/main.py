from unittest import case


#VARIABLES GLOBALES
#LISTA CONTIGUA
Lista_contigua = [0] * 10

#LISTA LIGADA
nodo = [[None, -1] for _ in range(10)]
cabeza = 0
actuall = 0
fin = 0

#LISTA DOBLEMENTE LIGADA
nodo_doble = [[None, -1, -1] for _ in range(10)]
cabeza_doble = 0
actual_doble = 0
fin_doble = 0
previo_doble = 0

#LISTA INDEXADA
lista_indexada = [0] * 10
indice = [0] * 10
############################## LISTA LIGADA #############################

def crear_lista_ligada():
    global cabeza, actuall, fin
    while True:
        num = input("Ingrese el dato (-1 para finalizar) :")
        if num == "-1":
            fin = -1
            break

        nodo[actuall][0] = num
        nodo[actuall][1] = cabeza - 1
        actuall = actuall + 1
        cabeza = actuall




        if actuall == 10:
            print("Datos completos")
            break


def eliminar_lista_ligada():
    global actuall, cabeza
    mostrar_lista_ligada()
    dato_eliminar = input("Ingrese el dato a eliminar: ")
    actuall = cabeza - 1
    previo = 0
    while actuall > -1:
        #print(nodo[actuall][0])

        if nodo[actuall][0] == dato_eliminar:
            if actuall == cabeza-1:
                cabeza -= 1
                print("Dato eliminado")
                return

            nodo[previo][1] = nodo[actuall][1]
            print("Dato eliminado")
            return
        previo = actuall
        actuall = nodo[actuall][1]
    print("Dato no encontrado")

def mostrar_lista_ligada():
    global actuall, cabeza
    if cabeza == -1:
        print("La lista está vacía.")
        return

    actuall = cabeza - 1
    print("------------------------------------------------")
    print("|        Datos        |        Siguiente       |")
    print("------------------------------------------------")
    while actuall > -1:
        if nodo[actuall][1] == -1:
            print(f"|          {nodo[actuall][0]}          |          None          |")
            #print(nodo[actuall][0])
            print("------------------------------------------------")

        else :
            print(f"|          {nodo[actuall][0]}          |            {nodo[nodo[actuall][1]][0]}           |")
            #print(nodo[actuall][0])
            print("------------------------------------------------")

        actuall = nodo[actuall][1]




############################# LISTA DOBLEMENTE LIGADA #######################

def crear_lista_doble_ligada():
    global cabeza_doble, actual_doble, fin_doble, previo_doble
    while True:
        num = input("Ingrese el dato (-1 para finalizar) :")
        if num == "-1":
            fin_doble = -1
            break
        if cabeza_doble == 0:
            nodo_doble[actual_doble][0] = num
            nodo_doble[actual_doble][1] = cabeza_doble - 1

            actual_doble = actual_doble + 1
            cabeza_doble = actual_doble
        else:
            nodo_doble[actual_doble][0] = num
            nodo_doble[actual_doble][1] = cabeza_doble - 1
            nodo_doble[previo_doble][2] = cabeza_doble
            previo_doble += 1
            actual_doble = actual_doble + 1
            cabeza_doble = actual_doble





        if actual_doble == 10:
            print("Datos completos")
            break


def eliminar_lista_doble_ligada():
    global actual_doble, cabeza_doble, previo_doble
    mostrar_lista_doble_ligada()
    dato_eliminar = input("Ingrese el dato a eliminar: ")
    actual_doble = cabeza_doble - 1
    previo_doble = 0
    while actual_doble > -1:
        #print(nodo[actuall][0])

        if nodo_doble[actual_doble][0] == dato_eliminar:
            if actual_doble == cabeza_doble-1:
                cabeza_doble -= 1
                print("Dato eliminado")
                return

            nodo_doble[previo_doble][1] = nodo_doble[actual_doble][1]
            if nodo_doble[actual_doble][1] != -1:
                nodo_doble[nodo_doble[actual_doble][1]][2] = nodo_doble[actual_doble][2]

            print("Dato eliminado")
            return
        previo_doble = actual_doble

        actual_doble = nodo_doble[actual_doble][1]
    print("Dato no encontrado")

def mostrar_lista_doble_ligada():
    global actual_doble, cabeza_doble
    if cabeza_doble == -1:
        print("La lista está vacía.")
        return

    actual_doble = cabeza_doble - 1
    print("-------------------------------------------------------------------------")
    print("|         Previo         |        Datos        |        Siguiente       |")
    print("-------------------------------------------------------------------------")
    while actual_doble > -1:
        if nodo_doble[actual_doble][1] == -1 and nodo_doble[actual_doble][2] == -1:
            print(f"|          None          |          {nodo_doble[actual_doble][0]}          |          None          |")
            print("-------------------------------------------------------------------------")
        elif nodo_doble[actual_doble][1] == -1:
            print(f"|            {nodo_doble[nodo_doble[actual_doble][2]][0]}           |          {nodo_doble[actual_doble][0]}          |          None          |")
            print("-------------------------------------------------------------------------")
        elif nodo_doble[actual_doble][2] == -1:
            print(f"|          None          |          {nodo_doble[actual_doble][0]}          |            {nodo_doble[nodo_doble[actual_doble][1]][0]}           |")
            print("-------------------------------------------------------------------------")
        else :
            print(f"|            {nodo_doble[nodo_doble[actual_doble][2]][0]}           |          {nodo_doble[actual_doble][0]}          |            {nodo_doble[nodo_doble[actual_doble][1]][0]}           |")
            print("-------------------------------------------------------------------------")

        actual_doble = nodo_doble[actual_doble][1]




############################# LISTA CONTIGUA ################################

def crear_lista_contigua():

    n = int(input("Ingrese la cantidad de elementos (maximo 10): "))
    if n > 10:
        print("Se excedio el limite de elementos de la lista.")
        return
    for i in range(n):
        dato = input(f"Ingrese el dato de la posicion {i}: ")
        Lista_contigua[i] = dato


def mostrar_lista_contigua():
    print("------------------------------------------------")
    print("|        Datos        |        Posicion        |")
    print("------------------------------------------------")
    for i in range(len(Lista_contigua)):
        if Lista_contigua[i] != 0:
            print(f"|          {Lista_contigua[i]}          |            {i}           |")
            print("------------------------------------------------")

    #print("------------------------------------------------")

def eliminar_lista_contigua():
    mostrar_lista_contigua()
    indice_eliminar = input("Ingrese el indice del valor que desea eliminar: ")
    for i in range(len(Lista_contigua)):
        if str(i) == indice_eliminar:
            Lista_contigua[i] = 0
            print("El indice ha sido eliminado")
            return

    print("El indice no existe en la lista contiguada")

############################# LISTA INDEXADA #################################

def crear_lista_indexada():
    global lista_indexada, indice
    n = int(input("Ingrese el número de elementos (maximo 10): "))


    if n > 10:
        print("Se excedio el limite de elementos de la lista.")
        return


    for i in range(n):
        lista_indexada[i] = input(f"Ingrese el elemento {i + 1}: ")
        indice[i] = i + 1  # Índices comienzan desde 1

def eliminar_lista_indexada():
    global lista_indexada, indice
    mostrar_lista_indexada()

    dato_eliminar = input("Ingrese el dato que desea eliminar: ")
    for i in range(len(lista_indexada)):
        if indice[i] != 0 and lista_indexada[i] == dato_eliminar:
            indice[i] = 0
            print("Dato eliminado")
            return

    print("dato no encontrado")



def mostrar_lista_indexada():
    global lista_indexada, indice
    print("---------------------------------------------")
    print("|        Datos        |        Indice       |")
    print("---------------------------------------------")



    for i in range(len(lista_indexada)):
        if indice[i] != 0:
            print(f"|          {lista_indexada[i]}          |          {indice[i]}          |")
            print("---------------------------------------------")


##############################################################################
def insertar_datos(lista : str):

    if lista == "1":
        crear_lista_contigua()
    elif lista == "2":
        crear_lista_ligada()
    elif lista == "3":
        crear_lista_doble_ligada()
    elif lista == "4":
        crear_lista_indexada()

def eliminar_datos(lista : str):
    if lista == "1":
        eliminar_lista_contigua()
    elif lista == "2":
        eliminar_lista_ligada()
    elif lista == "3":
        eliminar_lista_doble_ligada()
    elif lista == "4":
        eliminar_lista_indexada()

def mostrar_datos(lista : str):
    if lista == "1":
        mostrar_lista_contigua()
    elif lista == "2":
        mostrar_lista_ligada()
    elif lista == "3":
        mostrar_lista_doble_ligada()
    elif lista == "4":
        mostrar_lista_indexada()

def menu(lista : str):
    while(True):
        print("Seleccione una opcion:")
        print("1. Insertar Datos")
        print("2. Eliminar Datos")
        print("3. Mostrar datos visualmente")
        print("4. Salir")
        opcion = input("Selecciona una opcion:")
        match opcion:
            case "1":
                insertar_datos(lista)
            case "2":
                eliminar_datos(lista)
            case "3":
                mostrar_datos(lista)
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")


def main():

    while(True):
        print("Seleccione el tipo de lista a probar:")
        print("1. Lista Contigua")
        print("2. Lista Ligada")
        print("3. Lista Doblemente Ligada")
        print("4. Lista Indexada")
        print("5. Salir")
        opcion = input("Ingrese la opcion:")
        match opcion:
            case "1":
                print("Lista Contigua")
                menu("1")
            case "2":
                print("Lista Ligada")
                menu("2")
            case "3":
                print("Lista Doblemente Ligada")
                menu("3")
            case "4":
                print("Lista Indexada")
                menu("4")
            case "5":
                break
            case _:
                print("No selecciono una opcion valida")

    print("Saliendo...")

if __name__ == "__main__":
    main()