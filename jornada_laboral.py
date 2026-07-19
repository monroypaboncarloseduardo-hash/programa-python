Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Definición de la matriz: [Nombre, Lun, Mar, Mié, Jue, Vie]
... equipo_horas = [
...     ["Recurso A", 8, 8, 8, 8, 8],  # 40 horas
...     ["Recurso B", 9, 9, 9, 9, 9],  # 45 horas (Sobretiempo)
...     ["Recurso C", 6, 7, 6, 7, 6],  # 32 horas (Estándar/Inferior)
...     ["Recurso D", 10, 8, 8, 10, 8] # 44 horas (Sobretiempo)
... ]
...
... def procesar_jornadas(matriz, umbral=40):
...     """Calcula el total de horas y clasifica la jornada de cada recurso."""
...     print(f"{'Nombre':<15} | {'Total Horas':<12} | {'Clasificación'}")
...     print("-" * 45)
...
...     for fila in matriz:
...         nombre = fila[0]
...         # Sumamos los valores numéricos desde el índice 1 al 5
...         total_semanal = sum(fila[1:])
...
...         # Lógica de clasificación
...         if total_semanal > umbral:
...             clasificacion = "Sobretiempo"
...         else:
...             clasificacion = "Horario Estándar"
...
...         print(f"{nombre:<15} | {total_semanal:<12} | {clasificacion}")
...
... # Ejecución del módulo
... procesar_jornadas(equipo_horas)
...
Nombre          | Total Horas  | Clasificación
---------------------------------------------
Recurso A       | 40           | Horario Estándar
Recurso B       | 45           | Sobretiempo
Recurso C       | 32           | Horario Estándar
Recurso D       | 44           | Sobretiempo
>>>
>>>
>>>
>>>
>>> 44
44
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> ^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Z^Zzh
  File "<python-input-84>", line 1
    ␦␦␦␦␦␦␦␦␦␦␦␦␦␦␦␦␦␦zh
    ^
SyntaxError: invalid non-printable character U+001A
>>>
>>>
>>>
>>>
>>>
>>>
