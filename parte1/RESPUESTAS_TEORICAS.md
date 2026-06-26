# Respuestas teóricas — Parte 1 (Archivos)

Estas son las respuestas a las preguntas de la consigna. Sirven como guía
para la defensa; en el video conviene explicarlas con tus propias palabras.

---

## 1. ¿Para qué sirve el modo de apertura de un archivo?

El modo de apertura es el segundo parámetro de `open()` (por ejemplo
`open("notas.csv", "r")`). Le indica a Python **qué operaciones vamos a
permitir** sobre el archivo (leer, escribir, agregar) y **cómo se comporta**
con el contenido que ya existe (si lo conserva, si lo borra o si crea el
archivo en caso de que no exista). Elegir bien el modo evita errores y
evita borrar información por accidente.

## 2. ¿Qué diferencias existen entre "r", "w" y "a"?

- **`"r"` (read / lectura):** abre el archivo solo para **leer**. El puntero
  arranca al **principio**. El archivo **debe existir**; si no existe, da error.
  No permite escribir.

- **`"w"` (write / escritura):** abre el archivo para **escribir**. Si el
  archivo **no existe lo crea**, y si **ya existe borra todo su contenido**
  (lo trunca) y empieza de cero. El puntero arranca al principio.

- **`"a"` (append / agregar):** abre el archivo para **agregar** al final. Si
  no existe lo crea, y si existe **conserva** lo que había. El puntero se
  ubica al **final**, por lo que todo lo nuevo se escribe después del
  contenido anterior, sin borrarlo.

En este parcial usamos `"r"` para leer `notas.csv` y `"w"` para generar el
archivo nuevo con la fecha del día (queremos un archivo limpio cada vez).

## 3. ¿Es importante cerrar un archivo? Justificar.

Sí, es importante. Al cerrar el archivo con `archivo.close()`:

- Se **vuelca a disco** lo que estaba en el buffer en memoria. Si no cerramos,
  parte de lo que “escribimos” podría no quedar realmente guardado.
- Se **liberan los recursos** del sistema operativo (cada archivo abierto
  ocupa un descriptor/handle, que son limitados).
- Se **libera el archivo** para que otros programas o procesos puedan usarlo,
  y se evitan bloqueos o datos corruptos.

Una alternativa que cierra el archivo automáticamente es usar `with open(...)`.

## 4. ¿Qué es el puntero de un archivo (también llamado posición)?

Es una **marca interna** que indica en qué lugar del archivo se va a leer o
escribir **la próxima vez**. Se mide en caracteres/bytes desde el comienzo.

- Cada vez que leemos o escribimos, el puntero **avanza** automáticamente.
- Con `"r"` arranca en 0 (inicio); con `"a"` arranca al final.
- Se puede consultar con `tell()` y moverlo manualmente con `seek()`.

Por ejemplo, cuando recorremos el archivo línea por línea con un `for`, el
puntero va avanzando solo de una línea a la siguiente hasta llegar al final.
