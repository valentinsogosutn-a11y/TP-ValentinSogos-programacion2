# ============================================================
#  Prints.py
#  Funciones cuya unica responsabilidad es mostrar informacion.
# ============================================================


def mostrar_titulo():
    print("=" * 56)
    print("   SISTEMA DE EGRESADOS - TECNICATURA EN PROGRAMACION")
    print("=" * 56)


def mostrar_menu():
    print("\n------------------- MENU -------------------")
    print("1. Cargar alumnos")
    print("2. Mostrar egresados por plan")
    print("3. Mostrar egresados anteriores al anio 2000")
    print("4. Buscar alumno por nombre o apellido")
    print("5. Salon de la fama (promedio >= 9)")
    print("6. Salir")
    print("--------------------------------------------")


def mostrar_alumno(alumno):
    """Muestra los datos de un alumno en una linea."""
    print("  Legajo:", alumno["legajo"],
          "| Apellido:", alumno["apellido"],
          "| Nombre:", alumno["nombre"],
          "| Egreso:", alumno["egreso"],
          "| Plan:", alumno["plan"],
          "| Promedio:", alumno["nota_promedio"])


def mostrar_lista(lista):
    """Muestra todos los alumnos de una lista."""
    i = 0
    while i < len(lista):
        mostrar_alumno(lista[i])
        i += 1


def mostrar_mensaje(mensaje):
    print(mensaje)
