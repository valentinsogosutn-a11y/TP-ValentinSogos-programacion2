# ============================================================
#  Cadenas.py
#  Funciones propias para manejar cadenas (algoritmia de cadenas).
#  NO se usa ningun metodo de la clase str. Solo len(), indexar
#  y recorrer caracter por caracter.
# ============================================================

# Letras validas (incluye vocales con acento y la enie, en mayuscula y minuscula).
LETRAS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúüñÁÉÍÓÚÜÑ"

# Tablas para pasar a minuscula contemplando acentos y enie.
MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÜÑ"
MINUSCULAS = "abcdefghijklmnopqrstuvwxyzáéíóúüñ"


def longitud(cadena):
    """Devuelve la cantidad de caracteres (len esta permitido)."""
    return len(cadena)


def limpiar(cadena):
    """Quita espacios, saltos de linea y tabulaciones del inicio y final."""
    inicio = 0
    fin = len(cadena) - 1
    while inicio <= fin and (cadena[inicio] == " " or cadena[inicio] == "\n"
                             or cadena[inicio] == "\r" or cadena[inicio] == "\t"):
        inicio += 1
    while fin >= inicio and (cadena[fin] == " " or cadena[fin] == "\n"
                             or cadena[fin] == "\r" or cadena[fin] == "\t"):
        fin -= 1
    limpia = ""
    i = inicio
    while i <= fin:
        limpia += cadena[i]
        i += 1
    return limpia


def es_letra(caracter):
    """True si el caracter es una letra (incluye acentos y enie)."""
    i = 0
    while i < len(LETRAS):
        if caracter == LETRAS[i]:
            return True
        i += 1
    return False


def es_letra_o_espacio(caracter):
    if caracter == " ":
        return True
    return es_letra(caracter)


def tiene_al_menos_una_letra(cadena):
    i = 0
    while i < len(cadena):
        if es_letra(cadena[i]):
            return True
        i += 1
    return False


def es_solo_letras(cadena):
    """True si la cadena tiene solo letras (sin espacios, numeros ni simbolos)."""
    if len(cadena) == 0:
        return False
    i = 0
    while i < len(cadena):
        if not es_letra(cadena[i]):
            return False
        i += 1
    return True


def es_solo_letras_y_espacios(cadena):
    """True si la cadena tiene solo letras y/o espacios."""
    if len(cadena) == 0:
        return False
    i = 0
    while i < len(cadena):
        if not es_letra_o_espacio(cadena[i]):
            return False
        i += 1
    return True


def a_minuscula(cadena):
    """Convierte una cadena a minuscula sin usar metodos de str.
    Reemplaza cada mayuscula por su minuscula usando las tablas."""
    resultado = ""
    i = 0
    while i < len(cadena):
        c = cadena[i]
        reemplazo = c
        j = 0
        while j < len(MAYUSCULAS):
            if c == MAYUSCULAS[j]:
                reemplazo = MINUSCULAS[j]
            j += 1
        resultado += reemplazo
        i += 1
    return resultado


def contiene(texto, subcadena):
    """True si 'subcadena' aparece dentro de 'texto' (busqueda parcial).
    Se compara caracter por caracter, deslizando la subcadena sobre el texto."""
    n = len(texto)
    m = len(subcadena)
    if m == 0:
        return True
    if m > n:
        return False
    i = 0
    while i <= n - m:
        j = 0
        coincide = True
        while j < m and coincide:
            if texto[i + j] != subcadena[j]:
                coincide = False
            j += 1
        if coincide:
            return True
        i += 1
    return False


def contiene_sin_distinguir_mayusculas(texto, subcadena):
    """Igual que contiene(), pero pasando todo a minuscula primero,
    asi 'fer' encuentra 'Fernandez' o 'Fernando'."""
    return contiene(a_minuscula(texto), a_minuscula(subcadena))


# ---------- Conversiones numericas (sin int(), sin float(), sin metodos de str) ----------

def es_entero(cadena):
    """True si la cadena representa un entero (solo digitos)."""
    if len(cadena) == 0:
        return False
    i = 0
    if cadena[0] == "-":
        if len(cadena) == 1:
            return False
        i = 1
    while i < len(cadena):
        if cadena[i] < "0" or cadena[i] > "9":
            return False
        i += 1
    return True


def a_entero(cadena):
    """Convierte una cadena validada como entero a int."""
    negativo = False
    i = 0
    if cadena[0] == "-":
        negativo = True
        i = 1
    numero = 0
    while i < len(cadena):
        numero = numero * 10 + (ord(cadena[i]) - ord("0"))
        i += 1
    if negativo:
        numero = -numero
    return numero


def es_decimal(cadena):
    """True si la cadena representa un numero (entero o con un punto decimal),
    por ejemplo '9' o '8.5'."""
    if len(cadena) == 0:
        return False
    puntos = 0
    digitos = 0
    i = 0
    if cadena[0] == "-":
        if len(cadena) == 1:
            return False
        i = 1
    while i < len(cadena):
        c = cadena[i]
        if c == ".":
            puntos += 1
            if puntos > 1:        # no se permite mas de un punto
                return False
        elif c >= "0" and c <= "9":
            digitos += 1
        else:
            return False
        i += 1
    return digitos > 0


def a_decimal(cadena):
    """Convierte una cadena validada como decimal a float, separando la
    parte entera de la parte decimal y dividiendo por la potencia de 10."""
    negativo = False
    i = 0
    if cadena[0] == "-":
        negativo = True
        i = 1
    parte_entera = 0
    parte_decimal = 0
    divisor = 1
    despues_del_punto = False
    while i < len(cadena):
        c = cadena[i]
        if c == ".":
            despues_del_punto = True
        else:
            digito = ord(c) - ord("0")
            if despues_del_punto:
                parte_decimal = parte_decimal * 10 + digito
                divisor = divisor * 10
            else:
                parte_entera = parte_entera * 10 + digito
        i += 1
    numero = parte_entera + parte_decimal / divisor
    if negativo:
        numero = -numero
    return numero
