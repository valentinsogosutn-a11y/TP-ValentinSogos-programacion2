# ============================================================
#  Funciones.py
#  Funciones logicas que resuelven el problema trabajando sobre
#  la LISTA DE DICCIONARIOS (estructura principal).
#
#  Cada alumno es un diccionario con las claves:
#     legajo, nombre, apellido, egreso, plan, nota_promedio
#
#  No se usan max(), min() ni sum(): se implementan a mano.
#  Metodos de listas usados: append() y copy() (permitidos).
# ============================================================

import random
import Cadenas


def existe_legajo(lista, legajo):
    """True si ya hay un alumno con ese legajo en la lista."""
    i = 0
    while i < len(lista):
        if lista[i]["legajo"] == legajo:
            return True
        i += 1
    return False


def generar_legajo(lista):
    """Genera un legajo aleatorio de 6 cifras que no se repita.
    Vuelve a sortear mientras el legajo ya exista."""
    legajo = 0
    unico = False
    while not unico:
        legajo = random.randint(100000, 999999)   # siempre 6 cifras
        if not existe_legajo(lista, legajo):
            unico = True
    return legajo


def crear_alumno(legajo, nombre, apellido, egreso, plan, nota_promedio):
    """Arma y devuelve el diccionario de un alumno."""
    alumno = {}
    alumno["legajo"] = legajo
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido
    alumno["egreso"] = egreso
    alumno["plan"] = plan
    alumno["nota_promedio"] = nota_promedio
    return alumno


def filtrar_por_plan(lista, plan):
    """Devuelve una lista nueva con los alumnos del plan indicado."""
    encontrados = []
    i = 0
    while i < len(lista):
        if lista[i]["plan"] == plan:
            encontrados.append(lista[i])
        i += 1
    return encontrados


def filtrar_anteriores_a(lista, anio):
    """Devuelve los alumnos cuyo anio de egreso es menor al indicado."""
    encontrados = []
    i = 0
    while i < len(lista):
        if lista[i]["egreso"] < anio:
            encontrados.append(lista[i])
        i += 1
    return encontrados


def filtrar_por_promedio_minimo(lista, minimo):
    """Devuelve los alumnos con nota_promedio mayor o igual al minimo."""
    encontrados = []
    i = 0
    while i < len(lista):
        if lista[i]["nota_promedio"] >= minimo:
            encontrados.append(lista[i])
        i += 1
    return encontrados


def buscar_por_texto(lista, texto):
    """Busqueda avanzada: parcial y sin distinguir mayusculas/minusculas,
    sobre el nombre O el apellido. Devuelve todos los alumnos que coinciden
    (contempla coincidencias multiples)."""
    encontrados = []
    i = 0
    while i < len(lista):
        alumno = lista[i]
        coincide_nombre = Cadenas.contiene_sin_distinguir_mayusculas(alumno["nombre"], texto)
        coincide_apellido = Cadenas.contiene_sin_distinguir_mayusculas(alumno["apellido"], texto)
        if coincide_nombre or coincide_apellido:
            encontrados.append(alumno)
        i += 1
    return encontrados


def sumar_promedios(lista):
    """Suma propia de las notas promedio (no se permite sum())."""
    total = 0.0
    i = 0
    while i < len(lista):
        total += lista[i]["nota_promedio"]
        i += 1
    return total


def promedio_general(lista):
    """Promedio general de las notas promedio de la lista.
    Si la lista esta vacia devuelve 0.0 (valor util, no rompe)."""
    if len(lista) == 0:
        return 0.0
    return sumar_promedios(lista) / len(lista)


def ordenar_por_promedio_desc(lista):
    """Algoritmo de ordenamiento (burbuja) ADAPTADO para trabajar sobre una
    lista de diccionarios. Ordena de MAYOR a MENOR segun 'nota_promedio'.
    Trabaja sobre una copia para no modificar la lista original."""
    copia = lista.copy()
    n = len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            # Si el actual tiene menor promedio que el siguiente, se intercambian.
            if copia[j]["nota_promedio"] < copia[j + 1]["nota_promedio"]:
                temporal = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temporal
            j += 1
        i += 1
    return copia
