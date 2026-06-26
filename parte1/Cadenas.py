# ============================================================
#  Cadenas.py
#  Funciones propias para manejar cadenas (algoritmia de
#  cadenas vista en clase). NO se usa ningun metodo de la
#  clase str (nada de .split(), .strip(), .isdigit(), etc.).
#  Solo se permite len(), indexar y recorrer caracter a caracter.
# ============================================================


def limpiar(cadena):
    """Quita espacios, saltos de linea y tabulaciones del inicio y
    del final de una cadena, recorriendola manualmente."""
    inicio = 0
    fin = len(cadena) - 1

    # Avanzar el indice 'inicio' mientras haya espacios en blanco.
    while inicio <= fin and (cadena[inicio] == " " or cadena[inicio] == "\n"
                             or cadena[inicio] == "\r" or cadena[inicio] == "\t"):
        inicio += 1

    # Retroceder el indice 'fin' mientras haya espacios en blanco.
    while fin >= inicio and (cadena[fin] == " " or cadena[fin] == "\n"
                             or cadena[fin] == "\r" or cadena[fin] == "\t"):
        fin -= 1

    # Reconstruir la cadena ya limpia.
    limpia = ""
    i = inicio
    while i <= fin:
        limpia += cadena[i]
        i += 1
    return limpia


def es_entero(cadena):
    """Devuelve True si la cadena representa un numero entero
    (solamente digitos del 0 al 9), False en caso contrario."""
    if len(cadena) == 0:
        return False

    i = 0
    # Permitir un signo negativo opcional al inicio.
    if cadena[0] == "-":
        if len(cadena) == 1:   # solo el signo no es valido
            return False
        i = 1

    while i < len(cadena):
        caracter = cadena[i]
        if caracter < "0" or caracter > "9":
            return False
        i += 1
    return True


def a_entero(cadena):
    """Convierte una cadena (ya validada como entero) a int,
    sin usar int() ni metodos de str, multiplicando por 10."""
    negativo = False
    i = 0
    if cadena[0] == "-":
        negativo = True
        i = 1

    numero = 0
    while i < len(cadena):
        digito = ord(cadena[i]) - ord("0")
        numero = numero * 10 + digito
        i += 1

    if negativo:
        numero = -numero
    return numero


def separar_por_coma(linea):
    """Separa una linea por comas de forma manual y devuelve una
    lista con cada campo. Se dimensiona la lista de forma fija contando
    las comas previamente para evitar el uso de .append()."""
    
    # Contamos las comas manualmente para saber el tamaño exacto de la lista
    cantidad_comas = 0
    i = 0
    while i < len(linea):
        if linea[i] == ",":
            cantidad_comas += 1
        i += 1
        
    # El numero de campos es siempre la cantidad de comas + 1
    tamano_lista = cantidad_comas + 1
    partes = [None] * tamano_lista
    indice_partes = 0
    
    actual = ""
    i = 0
    while i < len(linea):
        caracter = linea[i]
        if caracter == ",":
            partes[indice_partes] = actual   # asignacion directa por indice
            indice_partes += 1
            actual = ""
        else:
            actual += caracter
        i += 1
        
    partes[indice_partes] = actual   # el ultimo campo
    return partes