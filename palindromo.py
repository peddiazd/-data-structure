def es_palindromo(texto):
    """
    Función recursiva que determina si una cadena es un palíndromo.
    Ignora mayúsculas y espacios.
    """

    # Preprocesamiento
    texto = texto.replace(" ", "").lower()

    # Caso base
    if len(texto) <= 1:
        return True

    # Si los extremos son distintos
    if texto[0] != texto[-1]:
        return False

    # Llamada recursiva
    return es_palindromo(texto[1:-1])


# =====================
# Pruebas correctas
# =====================

print("anita →", es_palindromo("anita"))                  # False
print("racecar →", es_palindromo("racecar"))              # True
print("python →", es_palindromo("python"))                # False
print("Anita lava la tina →", es_palindromo("Anita lava la tina"))  # True