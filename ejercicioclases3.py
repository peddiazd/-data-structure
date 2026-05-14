class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        # Retorna el precio total de este producto específico
        return self.precio * self.cantidad

    def __str__(self):
        # Este método define cómo se ve el objeto al imprimirlo
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.cantidad}"

# -------------------------------------------------------
# -------------------------------------------------------

def mostrar_inventario(productos):
    print("\n--- Inventario Completo ---")
    # Iteramos sobre la lista e imprimimos cada producto
    # (Python llamará automáticamente al método __str__ de cada uno)
    for p in productos:
        print(p)
    print("---------------------------")

def producto_mas_caro(productos):
    # Usamos max() con una clave lambda.
    # lambda p: p.precio le dice a Python: "Compara los objetos basándote en su atributo precio"
    # Asumimos que la lista no está vacía para evitar errores.
    if len(productos) > 0:
        return max(productos, key=lambda p: p.precio)
    else:
        return None

def valor_inventario(productos):
    # Usamos sum() con un generador.
    # Por cada producto p en la lista, calculamos p.valor_total() y los suma todos.
    return sum(p.valor_total() for p in productos)

# --- Ejemplo de cómo se usaría (para probar el código) ---
if __name__ == "__main__":
    # Creamos una lista de objetos Producto
    lista_productos = [
        Producto("Laptop", 1200.00, 5),
        Producto("Mouse", 25.50, 20),
        Producto("Monitor", 300.00, 10)
    ]

    # Probamos las funciones
    mostrar_inventario(lista_productos)
    
    caro = producto_mas_caro(lista_productos)
    if caro:
        print(f"\nEl producto más caro es: {caro.nombre}")
    
    total = valor_inventario(lista_productos)
    print(f"El valor total del inventario es: ${total:,.2f}")