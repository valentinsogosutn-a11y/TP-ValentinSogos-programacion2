# ============================================================
#  Archivos.py (Parte 2)
#  Funciones para LEER y GUARDAR la lista de diccionarios en
#  formato JSON (serializacion y deserializacion).
#  Se evita try/except: para no romper al abrir un archivo
#  inexistente, primero se verifica que exista (os.path.exists).
# ============================================================

import os
import json


def existe_archivo(nombre_archivo):
    """Indica si el archivo existe para evitar excepciones."""
    return os.path.exists(nombre_archivo)


def leer_alumnos(nombre_archivo):
    """Lee (deserializa) la lista de diccionarios desde un archivo JSON.
    Si el archivo no existe o esta vacio, devuelve una lista vacia."""
    if not existe_archivo(nombre_archivo):
        return []
        
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    
    # Manejo seguro si el archivo JSON existiera pero estuviese totalmente vacio
    try:
        datos = json.load(archivo)  # deserializacion: texto JSON -> lista de dicts
    except json.JSONDecodeError:
        datos = []
        
    archivo.close()
    return datos


def guardar_alumnos(nombre_archivo, lista):
    """Guarda (serializa) la lista de diccionarios en un archivo JSON,
    sobreescribiendo el contenido anterior. Devuelve True."""
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    
    # ensure_ascii=False conserva acentos legibles; indent ordena el archivo.
    json.dump(lista, archivo, ensure_ascii=False, indent=4)
    
    archivo.close()
    return True