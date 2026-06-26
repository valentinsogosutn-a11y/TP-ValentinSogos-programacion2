# ============================================================
#  Archivos.py
#  Funciones para LEER y GUARDAR archivos CSV.
#  IMPORTANTE: no se usa el modulo csv, ni csv.reader(),
#  ni csv.writer(). La lectura es linea por linea y la
#  separacion por comas es manual (modulo Cadenas).
# ============================================================

import os
import datetime
import Cadenas


def existe_archivo(nombre_archivo):
    """Indica si el archivo existe, para evitar que el programa se
    rompa al intentar abrir un archivo inexistente (sin try/except)."""
    return os.path.exists(nombre_archivo)


def leer_notas_csv(nombre_archivo):
    """Lee el archivo notas.csv LINEA POR LINEA, separa cada linea por
    comas manualmente y arma la matriz convirtiendo todo a enteros.

    Devuelve la matriz (lista de listas de enteros). Si el archivo no
    existe devuelve una lista vacia."""
    matriz = []

    if not existe_archivo(nombre_archivo):
        return matriz

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    # Se recorre el archivo una linea a la vez.
    for linea in archivo:
        linea = Cadenas.limpiar(linea)          # saca el salto de linea final
        if len(linea) > 0:                      # ignorar lineas vacias
            campos = Cadenas.separar_por_coma(linea)   # separacion manual por coma
            fila = []
            i = 0
            while i < len(campos):
                dato = Cadenas.limpiar(campos[i])
                if Cadenas.es_entero(dato):
                    fila.append(Cadenas.a_entero(dato))   # convertir a entero
                i += 1
            if len(fila) > 0:
                matriz.append(fila)

    archivo.close()
    return matriz


def guardar_notas_csv(matriz):
    """Guarda la matriz en un archivo CSV cuyo nombre es la FECHA ACTUAL
    en formato dd-mm-aaaa.csv (por ejemplo 01-07-2026.csv).

    La escritura tambien es manual: se arma cada linea concatenando los
    valores separados por comas (sin csv.writer()).
    Devuelve el nombre del archivo generado."""

    # Para obtener la fecha actual se usa el modulo datetime.
    hoy = datetime.date.today()
    nombre_archivo = hoy.strftime("%d-%m-%Y") + ".csv"

    archivo = open(nombre_archivo, "w", encoding="utf-8")

    i = 0
    while i < len(matriz):
        fila = matriz[i]
        linea = ""
        j = 0
        while j < len(fila):
            linea += str(fila[j])           # str() es una funcion, no un metodo de str
            if j < len(fila) - 1:           # poner coma entre valores, no al final
                linea += ","
            j += 1
        archivo.write(linea + "\n")
        i += 1

    archivo.close()
    return nombre_archivo
