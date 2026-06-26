# ============================================================
#  Inputs.py
#  Funciones de ingreso y validacion. No devuelven el control
#  hasta que el dato sea valido, de modo que el sistema sea
#  robusto y no se rompa ante ingresos invalidos.
# ============================================================

import Cadenas


def pedir_entero_en_rango(mensaje, minimo, maximo):
    """Pide un entero entre minimo y maximo (inclusive)."""
    valor = 0
    valido = False
    while not valido:
        entrada = Cadenas.limpiar(input(mensaje))
        if Cadenas.es_entero(entrada):
            numero = Cadenas.a_entero(entrada)
            if numero >= minimo and numero <= maximo:
                valor = numero
                valido = True
            else:
                print("  >> Debe estar entre", minimo, "y", maximo, ".")
        else:
            print("  >> Debe ingresar un numero entero.")
    return valor


def pedir_decimal_en_rango(mensaje, minimo, maximo):
    """Pide un numero (entero o decimal) entre minimo y maximo."""
    valor = 0.0
    valido = False
    while not valido:
        entrada = Cadenas.limpiar(input(mensaje))
        if Cadenas.es_decimal(entrada):
            numero = Cadenas.a_decimal(entrada)
            if numero >= minimo and numero <= maximo:
                valor = numero
                valido = True
            else:
                print("  >> Debe estar entre", minimo, "y", maximo, ".")
        else:
            print("  >> Debe ingresar un numero valido (ej: 8 o 8.5).")
    return valor


def pedir_nombre_o_apellido(que):
    """Pide un nombre o apellido valido:
        - minimo 3 caracteres
        - solo letras y espacios (sin numeros ni simbolos)
        - al menos una letra (que no sea todo espacios)."""
    valor = ""
    valido = False
    while not valido:
        entrada = Cadenas.limpiar(input("Ingrese " + que + ": "))
        if Cadenas.longitud(entrada) < 3:
            print("  >> Debe tener al menos 3 caracteres.")
        elif not Cadenas.es_solo_letras_y_espacios(entrada):
            print("  >> Solo se permiten letras y espacios (sin numeros ni simbolos).")
        elif not Cadenas.tiene_al_menos_una_letra(entrada):
            print("  >> Debe contener al menos una letra.")
        else:
            valor = entrada
            valido = True
    return valor


def pedir_plan():
    """Pide el plan, que solo puede ser 1991, 2003 o 2024."""
    valor = 0
    valido = False
    while not valido:
        print("Planes disponibles: 1991 / 2003 / 2024")
        entrada = Cadenas.limpiar(input("Ingrese el plan: "))
        if Cadenas.es_entero(entrada):
            numero = Cadenas.a_entero(entrada)
            if numero == 1991 or numero == 2003 or numero == 2024:
                valor = numero
                valido = True
            else:
                print("  >> Plan invalido. Debe ser 1991, 2003 o 2024.")
        else:
            print("  >> Debe ingresar un numero.")
    return valor


def pedir_texto_busqueda():
    """Pide un texto para buscar: minimo 3 caracteres y solo letras."""
    valor = ""
    valido = False
    while not valido:
        entrada = Cadenas.limpiar(input("Ingrese el texto a buscar (min 3 letras): "))
        if Cadenas.longitud(entrada) < 3:
            print("  >> Debe ingresar al menos 3 caracteres.")
        elif not Cadenas.es_solo_letras(entrada):
            print("  >> Solo se permiten letras.")
        else:
            valor = entrada
            valido = True
    return valor


def confirmar(mensaje):
    """Pide confirmacion al usuario (s/n) y devuelve True o False."""
    respuesta = ""
    while respuesta != "s" and respuesta != "n":
        respuesta = Cadenas.a_minuscula(Cadenas.limpiar(input(mensaje + " (s/n): ")))
        if respuesta != "s" and respuesta != "n":
            print("  >> Responda con 's' o 'n'.")
    return respuesta == "s"
