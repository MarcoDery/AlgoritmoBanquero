import time

necesarios_matriz = []
asignados_matriz = []
disponibles_matriz = []
existentes_matriz=[]
necesaros_asignados_matriz= []


def ingresar_datos_matriz_necesarios(matriz):
    for n in range(0, 4):
        fila = []
        for m in range(0, 3):
            while True:
                try:
                    numero = int(input(f"Inserta valor para la matriz necesarios en [{n}] [{m}]: "))
                    print(f"Valor {numero} ingresado correctamente en [{n}][{m}]")
                    fila.append(numero)
                    break
                except ValueError:
                    print("Inserta un valor numérico.")
        matriz.append(fila)

    for n in matriz:
        print(n)
def ingresar_datos_matriz_asignados(necesarios, asignados):
    for n in range(0, 4):
        fila = []
        for m in range(0, 3):
            while True:
                try:
                    numero = int(input(f"Inserta valor para la matriz asignados en [{n}] [{m}]: "))
                    if numero <= necesarios[n][m]:
                        print(f"Valor {numero} ingresado correctamente en [{n}][{m}]")
                        fila.append(numero)
                        break
                    else:
                        print("El valor de asignado es mayor al necesario. Vuelve a ingresarlo.")
                except ValueError:
                    print("Inserta un valor numérico.")
        asignados.append(fila)

    for n in asignados:
        print(n)

def ingresar_datos_matriz_existentes(matriz):
    for n in range(0, 3):
        while True:
            try:
                numero = int(input("Ingrese un valor para los recursos existentes: "))
                if numero in range(0, 10):
                    print("Valor guardado.")
                    matriz.append(numero)
                    break
                else:
                    print("Ingresa un valor entre 0 y 10.")
            except ValueError:
                print("Ingresa un número numérico.")

    print(f"Recursos existentes: {matriz}")

def ingresar_datos_matriz_disponibles(disponibles, existentes, asignados):
    for n in range(0, 3):
        while True:
            try:
                numero = int(input(f"Ingrese un valor para los recursos disponibles en la posición [{n}]: "))
                if numero <= existentes[n]:
                    suma_columna = sum(fila[n] for fila in asignados)
                    if numero <= suma_columna:  # Verificar si el número ingresado es menor o igual que la suma de la columna n de la matriz asignados
                        disponibles.append(numero)
                        break
                    else:
                        print(f"El valor ingresado {numero} es mayor que la suma de la columna {n} de la matriz asignados.")
                else:
                    print(f"El valor ingresado {numero} es mayor que el valor existente en la posición [{n}].")
            except ValueError:
                print("Inserta un valor numérico.")
    print(f"Recursos disponibles: {disponibles}")

def ingresar_datos():
    ingresar_datos_matriz_necesarios(necesarios_matriz)
    ingresar_datos_matriz_asignados(necesarios_matriz, asignados_matriz)
    ingresar_datos_matriz_existentes(existentes_matriz)
    ingresar_datos_matriz_disponibles(disponibles_matriz,existentes_matriz,asignados_matriz)

def mostrar_datos_4x3(matriz):
    for i, val in enumerate(matriz):
        print(f"P{i} {val}")
def mostrar_datos_1x3(matriz):
    print(matriz)

def necesarios_asignados(matriz1, matriz2):
    matriz = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            resultado = matriz1[i][j] - matriz2[i][j]
            fila.append(resultado)
        matriz.append(fila)
    return matriz

lista = []
def resolver_banquero(a, c_a, disponibles):
    while True:
        fila_cumple_condicion = None
        indice_fila = None
        for i, fila in enumerate(c_a):
            menor_o_igual = all(x <= y for x, y in zip(fila, disponibles))
            if menor_o_igual:
                fila_cumple_condicion = fila
                indice_fila = i
                break
        if fila_cumple_condicion == None:
            print("Ninguna fila cumple con la condición de ser menor o igual a A-C.")
            break
        else:
            suma_fila = [x + y for x, y in zip(a[indice_fila], fila_cumple_condicion)]
        #terminar código aquí
def menu():
    contador = 0
    while True:
        while contador == 0:
            print("==========================================================")
            print("==================ALGORITMO DEL BANQUERO==================")
            print("==========================================================")
            print("""Comenzaremos ingresando los datos a las matrices. 
    Esto tiene que ser en orden debido a que se tiene que asignar primero los necesarios ya que estos tienen que ser 
    siempre mayores a los asignados, se continua con los asignados, luego los recursos existentes y por último los 
    recursos disponibles. Estos son al último puesto que es necesario comparar que siempre sean menores que los 
    existentes y menores o iguales a la suma de los asignados en el recurso.""")
            time.sleep(5)

            print("\n\n")
            ingresar_datos()
            necesaros_asignados_matriz = necesarios_asignados(necesarios_matriz, asignados_matriz)
            contador += 1

        try:
            print("==================ALGORITMO DEL BANQUERO==================")
            print("1. Mostrar Recursos Necesarios. (C)")
            print("2. Mostrar Recursos Asignaods. (A)")
            print("3. Mostrar Recursos Existentes.")
            print("4. Mostrar Recursos Disponibles.")
            print("5. Mostrar Recursos Necesaros - Recursos Asignados. (C-A)")
            print("6. Resolver Algoritmo.")
            print("7. Salir.")

            opc = int(input("Ingrese una opción: "))

            if opc == 1:
                print("\nNECESARIOS")
                mostrar_datos_4x3(necesarios_matriz)
                input("Presione enter para continuar.")
            elif opc == 2:
                print("\nASIGNADOS")
                mostrar_datos_4x3(asignados_matriz)
                input("Presione enter para continuar.")
            elif opc == 3:
                print("\nEXISTENTES")
                mostrar_datos_1x3(existentes_matriz)
                input("Presione enter para continuar.")
            elif opc == 4:
                print("\nDISPONIBLES")
                mostrar_datos_1x3(disponibles_matriz)
                input("Presione enter para continuar.")
            elif opc == 5:
                print("\nNECESARIOS - ASIGNADOS")
                mostrar_datos_4x3(necesaros_asignados_matriz)
                input("Presione enter para continuar.")
            elif opc == 6:
                resolver_banquero(asignados_matriz,necesaros_asignados_matriz,disponibles_matriz)
            elif opc == 7:
                break
            else:
                print("Ingrese una opción valida.")
        except ValueError:
            print("Ingrese un valor correcto.")
            time.sleep(3)

menu()