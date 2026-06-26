# ============================================================
#  Menu.py (Parte 2)
#  Menu de opciones con toda la logica del programa de la Parte 2.
#  Conecta los modulos Prints, Inputs, Funciones y Archivos.
# ============================================================

import Prints
import Inputs
import Funciones
import Archivos

ARCHIVO_ALUMNOS = "alumnos.json"  # Constante del archivo definida en el flujo principal


def cargar_manual(lista):
    """Pide los datos de un alumno (el legajo se genera solo), arma el
    diccionario y pide confirmacion. Devuelve el alumno o None si se cancela."""
    nombre = Inputs.pedir_nombre_o_apellido("el nombre")
    apellido = Inputs.pedir_nombre_o_apellido("el apellido")
    egreso = Inputs.pedir_entero_en_rango("Ingrese el anio de egreso (1991-2026): ", 1991, 2026)
    plan = Inputs.pedir_plan()
    nota = Inputs.pedir_decimal_en_rango("Ingrese la nota promedio (6-10): ", 6, 10)

    # El legajo se genera aleatorio y unico (no lo ingresa el usuario).
    legajo = Funciones.generar_legajo(lista)
    alumno = Funciones.crear_alumno(legajo, nombre, apellido, egreso, plan, nota)

    print("\nDatos del alumno a registrar (legajo asignado:", legajo, "):")
    Prints.mostrar_alumno(alumno)

    if Inputs.confirmar("Confirma agregar este alumno?"):
        return alumno
    return None


def submenu_carga(lista):
    """Submenu de la opcion 1. Devuelve (lista, hubo_carga) donde
    'hubo_carga' es True si se cargaron datos correctamente."""
    print("\n-- Cargar alumnos --")
    print("  1. Cargar desde el archivo (alumnos.json)")
    print("  2. Carga manual")
    opcion = Inputs.pedir_entero_en_rango("Opcion de carga: ", 1, 2)

    if opcion == 1:
        datos = Archivos.leer_alumnos(ARCHIVO_ALUMNOS)  # Se pasa por parametro
        if len(datos) == 0:
            Prints.mostrar_mensaje("  >> No se encontraron datos en el archivo.")
            return lista, False
        
        # Los datos del archivo SOBREESCRIBEN la lista en memoria.
        nueva_lista = datos.copy()
        Prints.mostrar_mensaje("  >> Se cargaron " + str(len(nueva_lista)) + " alumnos desde el archivo.")
        return nueva_lista, True

    else:
        nuevo = cargar_manual(lista)
        if nuevo is not None:
            lista.append(nuevo)
            Prints.mostrar_mensaje("  >> Alumno agregado correctamente.")
            return lista, True
        else:
            Prints.mostrar_mensaje("  >> Carga cancelada.")
            return lista, False


def opcion_egresados_por_plan(lista):
    print("\n-- Egresados por plan --")
    plan = Inputs.pedir_plan()
    encontrados = Funciones.filtrar_por_plan(lista, plan)
    if len(encontrados) == 0:
        Prints.mostrar_mensaje(">> No hay alumnos recibidos del plan " + str(plan) + " todavia.")
    else:
        Prints.mostrar_mensaje("Egresados del plan " + str(plan) + ":")
        Prints.mostrar_lista(encontrados)


def opcion_anteriores_2000(lista):
    print("\n-- Egresados anteriores al anio 2000 --")
    encontrados = Funciones.filtrar_anteriores_a(lista, 2000)
    if len(encontrados) == 0:
        Prints.mostrar_mensaje(">> No hay egresados anteriores al anio 2000.")
    else:
        Prints.mostrar_lista(encontrados)
        promedio = Funciones.promedio_general(encontrados)
        Prints.mostrar_mensaje("Nota promedio general de los encontrados: " + str(round(promedio, 2)))


def opcion_buscar(lista):
    print("\n-- Buscar alumno por nombre o apellido --")
    texto = Inputs.pedir_texto_busqueda()
    encontrados = Funciones.buscar_por_texto(lista, texto)
    if len(encontrados) == 0:
        Prints.mostrar_mensaje(">> No se encontraron coincidencias.")
    else:
        Prints.mostrar_lista(encontrados)
        Prints.mostrar_mensaje("Cantidad de alumnos encontrados: " + str(len(encontrados)))


def opcion_salon_fama(lista):
    print("\n-- Salon de la fama (promedio >= 9) --")
    destacados = Funciones.filtrar_por_promedio_minimo(lista, 9)
    if len(destacados) == 0:
        Prints.mostrar_mensaje(">> ERROR: no hay alumnos con promedio mayor o igual a 9.")
    else:
        ordenados = Funciones.ordenar_por_promedio_desc(destacados)
        Prints.mostrar_lista(ordenados)


def opcion_salir(lista, cargados):
    """Antes de salir actualiza el archivo JSON (sobreescribiendo el anterior).
    Si nunca se cargaron datos, no se toca el archivo para no borrar la
    informacion existente."""
    if cargados:
        Archivos.guardar_alumnos(ARCHIVO_ALUMNOS, lista)  # Se pasa nombre y lista por parametro
        Prints.mostrar_mensaje("\nDatos guardados en " + ARCHIVO_ALUMNOS + ".")
    else:
        Prints.mostrar_mensaje("\nNo se cargaron datos: el archivo no se modifica.")
    Prints.mostrar_mensaje("Programa finalizado. Hasta luego!")


def ejecutar():
    """Bucle principal del programa."""
    Prints.mostrar_titulo()

    lista = []
    cargados = False
    opcion = 0

    while opcion != 6:
        Prints.mostrar_menu()
        opcion = Inputs.pedir_entero_en_rango("Elija una opcion: ", 1, 6)

        if opcion == 1:
            lista, hubo_carga = submenu_carga(lista)
            if hubo_carga:
                cargados = True

        elif opcion == 6:
            opcion_salir(lista, cargados)

        else:
            # Opciones 2 a 5: no se puede consultar/filtrar/ordenar sin cargar.
            if not cargados:
                Prints.mostrar_mensaje("\n>> Primero debe cargar alumnos (opcion 1).")
            else:
                if opcion == 2:
                    opcion_egresados_por_plan(lista)
                elif opcion == 3:
                    opcion_anteriores_2000(lista)
                elif opcion == 4:
                    opcion_buscar(lista)
                elif opcion == 5:
                    opcion_salon_fama(lista)