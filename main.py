import time
import app

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
                    numero = int(input(f"Inserta valor para la matriz C necesarios en [{n}] [{m}]: "))
                    fila.append(numero)
                    break
                except ValueError:
                    print("Inserta un valor numérico.")
        matriz.append(fila)
    
    print("\nC, Recursos Necesarios")
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
                        fila.append(numero)
                        break
                    else:
                        print("El valor de asignado es mayor al necesario. Vuelve a ingresarlo.")
                except ValueError:
                    print("Inserta un valor numérico.")
        asignados.append(fila)

    print("\nA, Recursos Asignados")
    for n in asignados:
        print(n)

def ingresar_datos_matriz_existentes(matriz):
    for n in range(0, 3):
        while True:
            try:
                numero = int(input("Ingrese un valor para los recursos existentes: "))
                if numero in range(0, 10):
                    matriz.append(numero)
                    break
                else:
                    print("Ingresa un valor entre 0 y 10.")
            except ValueError:
                print("Ingresa un número numérico.")

    print(f"\nRecursos existentes: {matriz}")

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
    print(f"\nRecursos disponibles: {disponibles}")

def ingresar_datos():
    ingresar_datos_matriz_necesarios(necesarios_matriz)
    ingresar_datos_matriz_asignados(necesarios_matriz, asignados_matriz)
    ingresar_datos_matriz_existentes(existentes_matriz)
    ingresar_datos_matriz_disponibles(disponibles_matriz,existentes_matriz,asignados_matriz)

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
            necesaros_asignados_matriz = app.necesarios_asignados(necesarios_matriz, asignados_matriz)
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
                app.mostrar_datos_4x3(necesarios_matriz)
                input("Presione enter para continuar.")
            elif opc == 2:
                print("\nASIGNADOS")
                app.mostrar_datos_4x3(asignados_matriz)
                input("Presione enter para continuar.")
            elif opc == 3:
                print("\nEXISTENTES")
                app.mostrar_datos_1x3(existentes_matriz)
                input("Presione enter para continuar.")
            elif opc == 4:
                print("\nDISPONIBLES")
                app.mostrar_datos_1x3(disponibles_matriz)
                input("Presione enter para continuar.")
            elif opc == 5:
                print("\nNECESARIOS - ASIGNADOS")
                app.mostrar_datos_4x3(necesaros_asignados_matriz)
                input("Presione enter para continuar.")
            elif opc == 6:
                app.banquero(disponibles_matriz, necesaros_asignados_matriz, asignados_matriz, necesarios_matriz)

            elif opc == 7:
                break
            else:
                print("Ingrese una opción valida.")
        except ValueError:
            print("Ingrese un valor correcto.")
            time.sleep(3)

menu()