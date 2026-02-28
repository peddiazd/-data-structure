def factorial(n: int) -> int:
    """
    Calcula el factorial de n de forma recursiva.
    Requisitos:
      - Sin bucles.
      - Lanza ValueError si n es negativo.
    """
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(0))   # 1
print(factorial(5))   # 120
print(factorial(10))  # 3628800
