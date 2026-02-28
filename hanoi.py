def hanoi(n, origen, destino, auxiliar):
    """
    Solución recursiva del problema de las Torres de Hanói.
    Imprime los movimientos necesarios para mover n discos
    desde 'origen' hasta 'destino' usando 'auxiliar'.
    """

    # Caso base: si no hay discos, no hacer nada
    if n == 0:
        return

    # 1. Mover n-1 discos al auxiliar
    hanoi(n - 1, origen, auxiliar, destino)

    # 2. Mover el disco n al destino
    print(f"Mover disco {n} de {origen} a {destino}")

    # 3. Mover los n-1 discos del auxiliar al destino
    hanoi(n - 1, auxiliar, destino, origen)


# =====================
# Prueba del programa
# =====================

hanoi(3, "A", "C", "B")