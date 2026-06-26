# ============================================================
#  Menu.py
#  Menu de opciones con toda la logica del programa de la Parte 1.
#  Conecta los modulos Prints, Inputs, Funciones y Archivos.
# ============================================================

import Prints
import Inputs
import Funciones
import Archivos

ARCHIVO_NOTAS = "notas.csv"   # archivo provisto por la catedra


def cargar_secuencial():
    """Carga manual de las notas de 7 alumnos x 3 trimestres.
    Cada nota se valida que sea un entero entre 1 y 10.
    Se inicializan las listas de forma fija sin usar .append()."""
    print("\n-- Carga secuencial --")
    
    # Inicializamos la matriz con el tamaño fijo de alumnos
    matriz = [None] * Funciones.CANTIDAD_ALUMNOS
    alumno = 0
    
    while alumno < Funciones.CANTIDAD_ALUMNOS:
        print("\nAlumno", alumno + 1, ":")
        
        # Inicializamos la fila con el tamaño fijo de trimestres
        fila = [0] * Funciones.CANTIDAD_TRIMESTRES
        trimestre = 0
        
        while trimestre < Funciones.CANTIDAD_TRIMESTRES:
            mensaje = "  Nota del trimestre " + str(trimestre + 1) + " (1 a 10): "
            nota = Inputs.pedir_entero_en_rango(mensaje, 1, 10)
            fila[trimestre] = nota  # asignacion directa por indice
            trimestre += 1
            
        matriz[alumno] = fila  # asignacion directa por indice
        alumno += 1
        
    return matriz


def cargar_desde_archivo():
    """Carga las notas leyendo el archivo notas.csv."""
    print("\n-- Carga desde archivo (notas.csv) --")
    if not Archivos.existe_archivo(ARCHIVO_NOTAS):
        Prints.mostrar_mensaje("  >> No se encontro el archivo " + ARCHIVO_NOTAS + ".")
        return []
    matriz = Archivos.leer_notas_csv(ARCHIVO_NOTAS)
    if len(matriz) == 0:
        Prints.mostrar_mensaje("  >> El archivo no contiene datos validos.")
    else:
        Prints.mostrar_mensaje("  >> Datos cargados correctamente desde el archivo.")
    return matriz


def opcion_cargar():
    """Submenu de carga. Devuelve (matriz, origen) o None si se cancela.
    'origen' vale 'manual' o 'archivo' para saber, al salir, si hay que
    guardar el CSV (solo se guarda si la carga fue manual)."""
    print("\nElija el tipo de carga:")
    print("  1. Carga secuencial (manual)")
    print("  2. Carga desde el archivo notas.csv")
    tipo = Inputs.pedir_entero_en_rango("Opcion de carga: ", 1, 2)

    if tipo == 1:
        matriz = cargar_secuencial()
        return matriz, "manual"
    else:
        matriz = cargar_desde_archivo()
        if len(matriz) == 0:
            return None
        return matriz, "archivo"


def opcion_salir(matriz, cargados, origen):
    """Al salir, si los datos fueron cargados MANUALMENTE, se guardan
    inmediatamente en un CSV cuyo nombre es la fecha actual."""
    if cargados and origen == "manual":
        nombre = Archivos.guardar_notas_csv(matriz)
        Prints.mostrar_mensaje("\nLos datos se guardaron en el archivo: " + nombre)
    Prints.mostrar_mensaje("Programa finalizado. Hasta luego!")


def ejecutar():
    """Bucle principal del programa."""
    Prints.mostrar_titulo()

    matriz = []
    cargados = False
    origen = ""
    opcion = 0

    while opcion != 6:
        Prints.mostrar_menu()
        opcion = Inputs.pedir_opcion_menu(1, 6)

        if opcion == 1:
            resultado = opcion_cargar()
            if resultado is not None:
                matriz = resultado[0]
                origen = resultado[1]
                cargados = True
                Prints.mostrar_matriz(matriz)

        elif opcion == 6:
            opcion_salir(matriz, cargados, origen)

        else:
            # Opciones 2 a 5: no se puede entrar sin haber cargado datos.
            if not cargados:
                Prints.mostrar_mensaje("\n>> Primero debe cargar las notas (opcion 1).")
            else:
                if opcion == 2:
                    indices = Funciones.alumnos_con_nota_menor_a(matriz, 7)
                    Prints.mostrar_alumnos_por_indices(
                        matriz, indices,
                        "Alumnos DESAPROBADOS (al menos una nota menor a 7):",
                        "No hay alumnos desaprobados.")

                elif opcion == 3:
                    indices = Funciones.alumnos_con_nota_menor_a(matriz, 4)
                    Prints.mostrar_alumnos_por_indices(
                        matriz, indices,
                        "Alumnos con APLAZOS (al menos una nota menor a 4):",
                        "No hay alumnos con aplazos.")

                elif opcion == 4:
                    porc_aprob, porc_desaprob = Funciones.porcentajes_aprobados_desaprobados(matriz)
                    Prints.mostrar_porcentajes(porc_aprob, porc_desaprob)

                elif opcion == 5:
                    promedios, mejor, ganadores = Funciones.trimestres_con_mejor_promedio(matriz)
                    Prints.mostrar_mejor_trimestre(promedios, ganadores)