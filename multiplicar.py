def multiplicar(a, b):
    """
    Función recursiva que calcula el producto de dos
    enteros no negativos usando únicamente sumas.
    """

    # Caso base: si b es 0, el resultado es 0
    if b == 0:
        return 0

    # Caso recursivo: a + multiplicar(a, b - 1)
    return a + multiplicar(a, b - 1)


# =====================
# Pruebas del programa
# =====================

print("4 x 3 →", multiplicar(4, 3))   # 12
print("7 x 0 →", multiplicar(7, 0))   # 0
print("0 x 9 →", multiplicar(0, 9))   # 0
print("6 x 6 →", multiplicar(6, 6))   # 36