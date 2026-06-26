# Segundo Parcial — Programación I (UTN Avellaneda)

Resolución del Segundo Parcial. El proyecto está dividido en dos partes,
cada una en su propia carpeta y con su propio menú de opciones.

## Estructura
parcial-programacion1/
├── parte1/                      # Matrices y archivos CSV
│   ├── Main.py                  # punto de entrada (solo invoca el menú)
│   ├── Menu.py                  # menú + lógica de control
│   ├── Prints.py                # salida de datos
│   ├── Inputs.py                # ingreso + validación
│   ├── Funciones.py             # lógica sobre la matriz
│   ├── Archivos.py              # leer/guardar CSV (manual, sin módulo csv)
│   ├── Cadenas.py               # algoritmia de cadenas propia
│   ├── notas.csv                # datos provistos (7 alumnos x 3 trimestres)
│   └── RESPUESTAS_TEORICAS.md   # respuestas teóricas de la defensa
│
└── parte2/                      # Listas de diccionarios y JSON
├── Main.py
├── Menu.py
├── Prints.py
├── Inputs.py
├── Funciones.py             # filtros, búsqueda, ordenamiento, legajo
├── Archivos.py              # leer/guardar JSON
├── Cadenas.py
└── alumnos.json             # datos de ejemplo (lista de diccionarios)

## Cómo ejecutar

Cada parte se ejecuta **parada dentro de su carpeta** (para que encuentre su
archivo de datos):

```bash
cd parte1
python Main.py
cd parte2
python Main.py


Restricciones respetadas
Parte 1:

Representación con matriz (lista de listas) estática, sin uso de .append().
Lectura/escritura de CSV algorítmica: línea por línea y separación manual
por coma. No se usa el módulo csv, ni csv.reader(), ni csv.writer().
Ningún método de la clase str: se implementaron funciones propias
(Cadenas.py).
Validaciones con algoritmia de cadenas; el programa no se rompe ante
ingresos inválidos y no utiliza bloques try/except.
No se accede a las opciones 2 a 5 sin haber cargado datos.
Al salir con carga manual se guarda un CSV con la fecha actual como
nombre (formato dd-mm-aaaa.csv, procesando de forma algorítmica y directa la marca de tiempo).

Parte 2:

Estructura principal: lista de diccionarios.
JSON para serializar/deserializar de forma modular pasando el nombre del archivo por parámetro.
Ningún método de la clase str (algoritmia propia en Cadenas.py).
Métodos de listas usados: solo append() y copy().
Sin max(), min() ni sum() (implementados a mano).
Sin list comprehension, sin operadores ternarios.
Legajo aleatorio de 6 cifras, único.
Algoritmo de ordenamiento (burbuja) adaptado a lista de diccionarios.
Búsqueda parcial e insensible a mayúsculas/minúsculas.
Se contemplan empates y coincidencias múltiples.
No se accede a consultas/filtros/ordenamiento sin cargar alumnos.
Reutilización de funciones (los filtros comparten la misma estructura algorítmica).