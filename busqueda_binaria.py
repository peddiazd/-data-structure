def busqueda_binaria(arr, objetivo, izq, der):
    """
    Búsqueda binaria recursiva. Retorna índice o -1 si no se encuentra.
    """
    if izq > der:
        return -1
    medio = (izq + der) // 2
    if arr[medio] == objetivo:
        return medio
    if arr[medio] < objetivo:
        return busqueda_binaria(arr, objetivo, medio + 1, der)
    return busqueda_binaria(arr, objetivo, izq, medio - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(busqueda_binaria(arr, 7, 0, len(arr) - 1))  # salida: 6
    print(busqueda_binaria(arr, 10, 0, len(arr) - 1)) # salida: -1