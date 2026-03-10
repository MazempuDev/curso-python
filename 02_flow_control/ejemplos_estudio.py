"""
Ejemplos de estudio para los temas en la carpeta `02_flow_control`:
- Sentencias condicionales (if, elif, else)
- Booleanos y operadores lógicos
- Listas (creación, acceso, slicing)
- Métodos de listas

Ejecutar: python ejemplos_estudio.py
"""

def separador(titulo: str):
    print("\n" + "-" * 10 + f" {titulo} " + "-" * 10)


def ejemplos_if():
    """Sentencias if, elif, else - control de flujo básico"""
    separador("IF - Condicionales simples")
    
    # if simple
    edad = 20
    if edad >= 18:
        print(f"Edad {edad}: Eres mayor de edad")
    
    # if-else
    edad = 15
    if edad >= 18:
        print(f"Edad {edad}: Eres mayor de edad")
    else:
        print(f"Edad {edad}: Eres menor de edad")
    
    # if-elif-else múltiples condiciones
    nota = 7.5
    if nota >= 9:
        print(f"Nota {nota}: ¡Sobresaliente!")
    elif nota >= 7:
        print(f"Nota {nota}: Notable")
    elif nota >= 5:
        print(f"Nota {nota}: Aprobado")
    else:
        print(f"Nota {nota}: Suspendido")
    
    # Condiciones múltiples con and/or
    edad = 25
    tiene_carnet = True
    if edad >= 18 and tiene_carnet:
        print(f"Puedes conducir (edad: {edad}, carnet: {tiene_carnet})")
    
    ingresos = 500
    if ingresos < 600 or ingresos > 3000:
        print(f"Ingresos especiales: ${ingresos}")


def ejemplos_booleans():
    """Valores booleanos y operadores lógicos"""
    separador("BOOLEANOS - Valores de verdad")
    
    # Valores booleanos básicos
    a = True
    b = False
    print(f"True es: {a} (tipo: {type(a)})")
    print(f"False es: {b} (tipo: {type(b)})")
    
    # Operadores de comparación
    print("\nOperadores de comparación:")
    print(f"5 > 3: {5 > 3}")
    print(f"5 < 3: {5 < 3}")
    print(f"5 == 5: {5 == 5}")
    print(f"5 != 3: {5 != 3}")
    print(f"5 >= 5: {5 >= 5}")
    print(f"3 <= 5: {3 <= 5}")
    
    # Comparación de cadenas
    print("\nComparación de cadenas:")
    print(f"'ana' < 'zebra': {'ana' < 'zebra'}")
    print(f"'hola' == 'Hola': {'hola' == 'Hola'}")
    print(f"'python' != 'java': {'python' != 'java'}")
    
    # Operadores lógicos: and, or, not
    print("\nOperadores lógicos:")
    print(f"True and True: {True and True}")
    print(f"True and False: {True and False}")
    print(f"True or False: {True or False}")
    print(f"not True: {not True}")
    
    # Evaluación en contexto booleano
    print("\nEvaluación en contexto booleano:")
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool('texto'): {bool('texto')}")
    print(f"bool(''): {bool('')}")
    print(f"bool([1,2]): {bool([1,2])}")
    print(f"bool([]): {bool([])}")


def ejemplos_listas():
    """Creación, acceso e índices de listas"""
    separador("LISTAS - Creación y acceso")
    
    # Crear listas
    print("\nCrear diferentes tipos de listas:")
    numeros = [1, 2, 3, 4, 5]
    frutas = ["manzana", "pera", "plátano"]
    mixta = [1, "hola", 3.14, True]
    vacia = []
    anidada = [[1, 2], [3, 4], [5, 6]]
    
    print(f"numeros: {numeros}")
    print(f"frutas: {frutas}")
    print(f"mixta: {mixta}")
    print(f"vacía: {vacia}")
    print(f"anidada: {anidada}")
    
    # Acceso por índice (positivo y negativo)
    print("\nAcceso por índice:")
    print(f"frutas[0]: {frutas[0]}")  # Primer elemento
    print(f"frutas[2]: {frutas[2]}")  # Tercer elemento
    print(f"frutas[-1]: {frutas[-1]}")  # Último elemento
    print(f"frutas[-2]: {frutas[-2]}")  # Penúltimo elemento
    print(f"anidada[1][0]: {anidada[1][0]}")  # Elemento de lista anidada
    
    # Slicing (rebanadas)
    print("\nSlicing - obtener porciones de la lista:")
    print(f"numeros[1:4]: {numeros[1:4]}")  # Índices 1, 2, 3
    print(f"numeros[:3]: {numeros[:3]}")    # Primeros 3 elementos
    print(f"numeros[2:]: {numeros[2:]}")    # Desde índice 2 al final
    print(f"numeros[::2]: {numeros[::2]}")  # Cada 2 elementos (saltos)
    print(f"numeros[::-1]: {numeros[::-1]}")# En orden inverso
    
    # Propiedades de listas
    print("\nPropiedades de listas:")
    print(f"len(frutas): {len(frutas)}")
    print(f"'manzana' in frutas: {'manzana' in frutas}")
    print(f"'uva' in frutas: {'uva' in frutas}")
    print(f"frutas.count('manzana'): {frutas.count('manzana')}")
    print(f"frutas.index('pera'): {frutas.index('pera')}")
    
    # Modificación simple
    print("\nModificación de elementos:")
    frutas[0] = "naranja"
    print(f"Después cambiar frutas[0]: {frutas}")


def ejemplos_metodos_listas():
    """Métodos importantes para manipular listas"""
    separador("MÉTODOS DE LISTAS - Manipulación")
    
    # append() - añadir al final
    print("\nmethod: append() - añadir un elemento al final")
    lista = ['a', 'b', 'c']
    lista.append('d')
    print(f"Después append('d'): {lista}")
    
    # insert() - insertar en posición
    print("\nmethod: insert(índice, valor) - insertar en posición específica")
    lista.insert(1, 'X')
    print(f"Después insert(1, 'X'): {lista}")
    
    # extend() - agregar múltiples elementos
    print("\nmethod: extend(iterable) - agregar múltiples elementos")
    lista.extend(['Y', 'Z'])
    print(f"Después extend(['Y', 'Z']): {lista}")
    
    # remove() - eliminar primer elemento con valor
    print("\nmethod: remove(valor) - eliminar primera aparición")
    lista.remove('X')
    print(f"Después remove('X'): {lista}")
    
    # pop() - eliminar por índice y devolver el valor
    print("\nmethod: pop(índice) - eliminar y devolver elemento")
    lista = ['a', 'b', 'c', 'd', 'e']
    ultimo = lista.pop()  # Elimina el último
    print(f"pop() devolvió: {ultimo}, lista ahora: {lista}")
    segundo = lista.pop(1)  # Elimina índice 1
    print(f"pop(1) devolvió: {segundo}, lista ahora: {lista}")
    
    # clear() - limpiar lista
    print("\nmethod: clear() - eliminar todos los elementos")
    temporal = [1, 2, 3]
    temporal.clear()
    print(f"Después clear(): {temporal}")
    
    # sort() - ordenar modificando la original
    print("\nmethod: sort() - ordenar la lista (modifica la original)")
    numeros = [3, 1, 4, 1, 5, 9, 2, 6]
    numeros.sort()
    print(f"Después sort(): {numeros}")
    
    # reverse() - invertir orden
    print("\nmethod: reverse() - invertir el orden")
    numeros = [1, 2, 3, 4, 5]
    numeros.reverse()
    print(f"Después reverse(): {numeros}")
    
    # copy() - crear una copia
    print("\nmethod: copy() - crear una copia independiente")
    original = [1, 2, 3]
    copia = original.copy()
    copia.append(4)
    print(f"original: {original}")
    print(f"copia modificada: {copia}")


def mini_ejercicios():
    """Ejercicios prácticos con soluciones rápidas"""
    separador("MINI-EJERCICIOS - Con soluciones")
    
    # 1) Determinar si número es positivo, negativo o cero
    print("\n1) Clasificar número:")
    numero = -5
    if numero > 0:
        resultado = "positivo"
    elif numero < 0:
        resultado = "negativo"
    else:
        resultado = "cero"
    print(f"{numero} es {resultado}")
    
    # 2) Validar si puede entrar a una película
    print("\n2) Acceso a película:")
    edad = 15
    tiene_dinero = True
    if edad >= 13 and tiene_dinero:
        print(f"Edad {edad}, dinero: {tiene_dinero} → Puedes entrar")
    else:
        print(f"Edad {edad}, dinero: {tiene_dinero} → No puedes entrar")
    
    # 3) Encontrar el mayor de tres números
    print("\n3) Máximo de tres números:")
    a, b, c = 10, 25, 15
    mayor = max(a, b, c)
    print(f"Mayor entre {a}, {b}, {c} es: {mayor}")
    
    # 4) Contar elementos de una lista que cumplen condición
    print("\n4) Contar números mayores a 5:")
    numeros = [2, 8, 3, 9, 1, 6, 4]
    mayores = [n for n in numeros if n > 5]
    print(f"Lista: {numeros}")
    print(f"Mayores a 5: {mayores} (cantidad: {len(mayores)})")
    
    # 5) Crear lista de pares de números
    print("\n5) Listar números pares:")
    pares = [n for n in range(1, 11) if n % 2 == 0]
    print(f"Pares del 1 al 10: {pares}")
    
    # 6) Procesar lista con múltiples operaciones
    print("\n6) Procesar lista (append, remove, sort):")
    datos = [3, 1, 4, 1, 5]
    datos.append(9)
    datos.remove(1)
    datos.sort()
    print(f"Resultado final: {datos}")
    
    # 7) Obtener información de un string (también es una secuencia)
    print("\n7) Analizar palabra:")
    palabra = "python"
    print(f"Palabra: {palabra}")
    print(f"Longitud: {len(palabra)}")
    print(f"Primera letra: {palabra[0]}")
    print(f"Últimas 3 letras: {palabra[-3:]}")
    print(f"Inverso: {palabra[::-1]}")
    
    # 8) Validar lista no vacía antes de acceder
    print("\n8) Acceso seguro a lista:")
    valores = [10, 20, 30]
    if valores:
        print(f"Lista tiene elementos. Primero: {valores[0]}")
    else:
        print("Lista vacía")


if __name__ == "__main__":
    ejemplos_if()
    ejemplos_booleans()
    ejemplos_listas()
    ejemplos_metodos_listas()
    mini_ejercicios()
    
    print("\n" + "=" * 50)
    print("Ejemplos completados. Estudia cada sección con cuidado.")
    print("=" * 50 + "\n")
