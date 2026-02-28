def suma_digitos(n: int) -> int:
    """
    Suma de los dígitos de un entero positivo de forma recursiva.

    Requisitos:
    - Caso base: n < 10, retornar n.
    - Caso recursivo: (n % 10) + suma_digitos(n // 10)

    Args:
        n (int): entero no negativo cuyo dígito se sumará.

    Returns:
        int: suma de los dígitos de n.

    Raises:
        ValueError: si n es negativo.
        TypeError: si n no es entero.
    """
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    if n < 0:
        raise ValueError("n debe ser no negativo")

    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejemplos de uso
print(suma_digitos(1234))  # 10