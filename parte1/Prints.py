# ============================================================
#  Prints.py
#  Funciones cuya UNICA responsabilidad es mostrar informacion
#  por pantalla. No calculan nada: reciben los datos ya
#  procesados por el modulo Funciones.
# ============================================================


def mostrar_titulo():
    print("=" * 54)
    print("     REGISTRO DE NOTAS - MATEMATICA (3 TRIMESTRES)")
    print("=" * 54)


def mostrar_menu():
    print("\n------------------- MENU -------------------")
    print("1. Cargar notas")
    print("2. Mostrar alumnos desaprobados")
    print("3. Mostrar alumnos con aplazos")
    print("4. Mostrar porcentaje de aprobados y desaprobados")
    print("5. Mostrar trimestre con mejor promedio")
    print("6. Salir")
    print("--------------------------------------------")


def mostrar_matriz(matriz):
    """Muestra toda la matriz de notas en forma de tabla."""
    print("\nNotas cargadas:")
    print("           | Trim 1 | Trim 2 | Trim 3")
    print("-------------------------------------")
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        linea = "Alumno " + str(i + 1) + "  |"
        j = 0
        while j < len(fila):
            linea += "   " + str(fila[j]) + "  |"
            j += 1
        print(linea)
        i += 1


def mostrar_alumnos_por_indices(matriz, indices, titulo, mensaje_si_vacio):
    """Muestra los alumnos cuyos indices se reciben en la lista 'indices'.
    Si la lista esta vacia, muestra el mensaje informativo."""
    print("\n" + titulo)
    if len(indices) == 0:
        print("  " + mensaje_si_vacio)
    else:
        k = 0
        while k < len(indices):
            indice = indices[k]
            fila = matriz[indice]
            linea = "  Alumno " + str(indice + 1) + " -> notas:"
            j = 0
            while j < len(fila):
                linea += " " + str(fila[j])
                j += 1
            print(linea)
            k += 1


def mostrar_porcentajes(porc_aprobados, porc_desaprobados):
    print("\nPorcentajes:")
    print("  Aprobados:    ", round(porc_aprobados, 2), "%")
    print("  Desaprobados: ", round(porc_desaprobados, 2), "%")


def mostrar_mejor_trimestre(promedios, ganadores):
    """Muestra el promedio de cada trimestre y cual fue el mejor,
    contemplando empates."""
    print("\nPromedio por trimestre:")
    t = 0
    while t < len(promedios):
        print("  Trimestre", t + 1, "->", round(promedios[t], 2))
        t += 1

    if len(ganadores) == 1:
        print("El trimestre con mejor promedio fue el Trimestre", ganadores[0])
    else:
        # Hubo empate entre varios trimestres.
        texto = ""
        i = 0
        while i < len(ganadores):
            texto += str(ganadores[i])
            if i < len(ganadores) - 1:
                texto += " y "
            i += 1
        print("Hubo un EMPATE entre los trimestres:", texto)


def mostrar_mensaje(mensaje):
    print(mensaje)
