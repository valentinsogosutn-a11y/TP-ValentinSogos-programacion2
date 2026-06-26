# ============================================================
#  Archivos.py
#  Funciones para LEER y GUARDAR la lista de diccionarios en
#  formato JSON (serializacion y deserializacion).
#  Se evita try/except: para no romper al abrir un archivo
#  inexistente, primero se verifica que exista (os.path.exists).
# ============================================================

import os
import json

ARCHIVO = "alumnos.json"


def existe_archivo(nombre_archivo):
    """True si el archivo existe."""
    return os.path.exists(nombre_archivo)


def leer_alumnos():
    """Lee (deserializa) la lista de diccionarios desde alumnos.json.
    Si el archivo no existe, devuelve una lista vacia."""
    if not existe_archivo(ARCHIVO):
        return []
    archivo = open(ARCHIVO, "r", encoding="utf-8")
    datos = json.load(archivo)       # deserializacion: texto JSON -> lista de dicts
    archivo.close()
    return datos


def guardar_alumnos(lista):
    """Guarda (serializa) la lista de diccionarios en alumnos.json,
    sobreescribiendo el contenido anterior. Devuelve True."""
    archivo = open(ARCHIVO, "w", encoding="utf-8")
    # ensure_ascii=False conserva acentos legibles; indent ordena el archivo.
    json.dump(lista, archivo, ensure_ascii=False, indent=4)
    archivo.close()
    return True
