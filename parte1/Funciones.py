# ============================================================
#  Funciones.py
#  Funciones logicas que resuelven el problema trabajando
#  sobre la matriz de notas.
#
#  La matriz es una lista de listas:
#     - cada fila  = un alumno
#     - cada columna = un trimestre (0 -> Trim 1, 1 -> Trim 2, 2 -> Trim 3)
#
#  No se usan max(), min() ni sum(): se implementan a mano.
# ============================================================

CANTIDAD_ALUMNOS = 7        # alumnos a cargar en la carga secuencial
CANTIDAD_TRIMESTRES = 3     # trimestres a cargar en la carga secuencial


def crear_matriz_vacia():
    """Crea una matriz de CANTIDAD_ALUMNOS x CANTIDAD_TRIMESTRES
    llena de ceros (no se usa en la carga, queda como utilitario)."""
    matriz = []
    i = 0
    while i < CANTIDAD_ALUMNOS:
        fila = []
        j = 0
        while j < CANTIDAD_TRIMESTRES:
            fila.append(0)
            j += 1
        matriz.append(fila)
        i += 1
    return matriz


def tiene_nota_menor_a(fila, umbral):
    """Devuelve True si el alumno (fila) tiene AL MENOS una nota
    menor al umbral. Se reutiliza para desaprobados (umbral 7) y
    para aplazos (umbral 4)."""
    j = 0
    while j < len(fila):
        if fila[j] < umbral:
            return True
        j += 1
    return False


def alumnos_con_nota_menor_a(matriz, umbral):
    """Devuelve una lista con los indices (0..n) de los alumnos que
    tengan al menos una nota menor al umbral."""
    indices = []
    i = 0
    while i < len(matriz):
        if tiene_nota_menor_a(matriz[i], umbral):
            indices.append(i)
        i += 1
    return indices


def esta_aprobado(fila):
    """Un alumno esta aprobado cuando NINGUNA de sus notas es menor a 7
    (es decir, todas sus notas son 7 o mas)."""
    return not tiene_nota_menor_a(fila, 7)


def contar_aprobados(matriz):
    """Cuenta cuantos alumnos estan aprobados (todas las notas >= 7)."""
    aprobados = 0
    i = 0
    while i < len(matriz):
        if esta_aprobado(matriz[i]):
            aprobados += 1
        i += 1
    return aprobados


def porcentajes_aprobados_desaprobados(matriz):
    """Devuelve (porc_aprobados, porc_desaprobados) como porcentajes."""
    total = len(matriz)
    if total == 0:
        return 0.0, 0.0
    aprobados = contar_aprobados(matriz)
    desaprobados = total - aprobados
    porc_aprobados = aprobados * 100 / total
    porc_desaprobados = desaprobados * 100 / total
    return porc_aprobados, porc_desaprobados


def promedio_columna(matriz, columna):
    """Calcula el promedio de un trimestre (columna) entre todos los
    alumnos. Suma manual (sin sum())."""
    total = 0
    i = 0
    while i < len(matriz):
        total += matriz[i][columna]
        i += 1
    return total / len(matriz)


def _son_iguales(a, b):
    """Compara dos numeros con coma con una pequena tolerancia, para
    poder detectar empates de promedios de forma segura."""
    diferencia = a - b
    if diferencia < 0:
        diferencia = -diferencia
    return diferencia < 0.000001


def trimestres_con_mejor_promedio(matriz):
    """Calcula el promedio de cada trimestre y devuelve:
        - la lista completa de promedios
        - el mejor promedio
        - una lista con los numeros de trimestre (1, 2, 3) que tienen
          ese mejor promedio (puede haber empate -> mas de uno).
    Se busca el maximo a mano (sin max())."""
    cantidad_trimestres = len(matriz[0])

    # 1) Calcular el promedio de cada trimestre.
    promedios = []
    j = 0
    while j < cantidad_trimestres:
        promedios.append(promedio_columna(matriz, j))
        j += 1

    # 2) Buscar el mejor promedio recorriendo la lista (sin max()).
    mejor = promedios[0]
    k = 1
    while k < len(promedios):
        if promedios[k] > mejor:
            mejor = promedios[k]
        k += 1

    # 3) Recolectar TODOS los trimestres que igualan el mejor (empates).
    ganadores = []
    t = 0
    while t < len(promedios):
        if _son_iguales(promedios[t], mejor):
            ganadores.append(t + 1)   # +1 para mostrar Trimestre 1, 2 o 3
        t += 1

    return promedios, mejor, ganadores
