"""
Ejemplos de estudio para los temas en la carpeta `01_basic`:
- Print
- Types
- Casting
- Variables
- Input (comentado para no bloquear)

Ejecutar: python ejemplos_estudio.py
"""

def separador(titulo: str):
    print("\n" + "-" * 10 + f" {titulo} " + "-" * 10)


def ejemplos_print():
    separador("Print")
    print("Hola mundo")
    print("Varios", "argumentos", 1, 2, 3)
    nombre = "Luis"
    edad = 30
    print(f"{nombre} tiene {edad} años")


def ejemplos_types():
    separador("Tipos de datos")
    valores = [10, 3.14, "texto", True, [1, 2], (3, 4), {5, 6}, {"k": "v"}]
    for v in valores:
        print(v, "->", type(v))


def ejemplos_casting():
    separador("Casting / Conversiones")
    s = "5"
    i = int(s)
    f = float("2.5")
    print("s (str):", s, "-> type:", type(s))
    print("int(s) + 3 ->", i + 3)
    print("float('2.5') * 2 ->", f * 2)
    # Conversion implícita en operaciones numéricas
    print("int + float ->", type(i + f), "value:", i + f)


def ejemplos_variables():
    separador("Variables")
    a = 100
    b = 200
    print("Antes: a=", a, "b=", b)
    # Intercambio pythonico
    a, b = b, a
    print("Después intercambio: a=", a, "b=", b)
    # Constante por convención
    PI = 3.14159
    print("PI:", PI)


def ejemplos_input():
    separador("Input (comentado)")
    print("Ejemplo de uso de input() está comentado para no bloquear la ejecución.")
    print("# name = input('¿Cómo te llamas? ')")
    print("# print(f'Hola, {name}')")


def mini_ejercicios():
    separador("Mini-ejercicios (con soluciones rápidas)")
    # 1) Sumar dos números (ejemplo)
    x = 7
    y = 8
    print("1) Suma:", x, "+", y, "=", x + y)

    # 2) Obtener el primer y último carácter de una cadena
    s = "python"
    print("2) Primera y última letra de 'python':", s[0], s[-1])

    # 3) Convertir lista de strings a enteros
    lista_str = ["1", "2", "3"]
    lista_int = [int(i) for i in lista_str]
    print("3) Lista convertida:", lista_int)


if __name__ == "__main__":
    ejemplos_print()
    ejemplos_types()
    ejemplos_casting()
    ejemplos_variables()
    ejemplos_input()
    mini_ejercicios()
