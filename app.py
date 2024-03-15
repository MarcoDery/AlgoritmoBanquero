import time
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

def banquero(disponibles_matriz, c_a, asignados_matriz, necesarios_matriz):
    while True:
        print("\nRecursos Disponibles")
        mostrar_datos_1x3(disponibles_matriz)

        print("\nC-A")
        for n_proceso, fila_c_a in enumerate(c_a):
            menor_o_igual = all(x <= y for x, y in zip(fila_c_a, disponibles_matriz))
            if menor_o_igual:
                print("\033[37mP{} {} \033[32mOKAY\033[0m".format(n_proceso, fila_c_a))
                asignados_matriz[n_proceso] = [x + y for x, y in zip(fila_c_a, asignados_matriz[n_proceso])]
                disponibles_matriz          = [x - y for x, y in zip(disponibles_matriz, c_a[n_proceso])]
                c_a[n_proceso]              = [x - y for x, y in zip(fila_c_a, c_a[n_proceso])]
            
            else:
                print("\033[37mP{} {} \033[31mBlock\033[0m".format(n_proceso, fila_c_a))
            time.sleep(.5)
        
        print("\nAsignando Recursos...")
        print("\nA")
        mostrar_datos_4x3(asignados_matriz)

        print("\nRecursos Disponibles")
        mostrar_datos_1x3(disponibles_matriz)

        print("\nLiberando recursos...")
        time.sleep(1.5)

        print("\nC-A")
        for n_proceso, fila_c_a in enumerate(c_a):
            if all(x == 0 for x in fila_c_a):
                print("\033[37mP{} {} \033[32mDONE\033[0m".format(n_proceso, fila_c_a))
            else:
                print("P{} {}".format(n_proceso, fila_c_a))
                
            if necesarios_matriz[n_proceso] == asignados_matriz[n_proceso]:
                disponibles_matriz          = [x + y for x, y in zip(disponibles_matriz, asignados_matriz[n_proceso])]
                asignados_matriz[n_proceso] = [0] * len(asignados_matriz[n_proceso])
            

        print("\nA")
        for n_proceso, fila_c_a in enumerate(asignados_matriz):
            if all(x == 0 for x in fila_c_a):
                print("\033[37mP{} {} \033[32mDONE\033[0m".format(n_proceso, fila_c_a))
            else:
                print("P{} {}".format(n_proceso, fila_c_a))

        print("\nRecursos Disponibles")
        mostrar_datos_1x3(disponibles_matriz)
        input("Presione enter para continuar.\n")
        todos_ceros = all(all(x == 0 for x in fila) for fila in asignados_matriz)
        if todos_ceros:
            print("No hay mas procesos solicitados\n")
            break
        else:
            continue