# ============================================================
#  Inputs.py
#  Funciones de ingreso y validacion de datos.
#  Toda la validacion se hace con algoritmia de cadenas
#  (modulo Cadenas) para que el programa NO se rompa ante
#  ingresos invalidos.
# ============================================================

import Cadenas


def pedir_entero_en_rango(mensaje, minimo, maximo):
    """Pide un numero entero por teclado y no devuelve el control
    hasta que el ingreso sea valido y este dentro del rango pedido.
    De esta forma el programa nunca se rompe."""
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
                print("  >> El valor debe estar entre", minimo, "y", maximo, ". Intente de nuevo.")
        else:
            print("  >> Entrada invalida. Debe ingresar un numero entero.")
    return valor


def pedir_opcion_menu(minimo, maximo):
    """Caso particular de pedir_entero_en_rango para elegir una
    opcion del menu."""
    return pedir_entero_en_rango("Elija una opcion: ", minimo, maximo)
