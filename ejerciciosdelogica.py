# ==========================================
# BLOQUE 1: CONDICIONALES (IF / ELSE)
# ==========================================

# -------------------------------------------------------
# 1. Par o impar
# -------------------------------------------------------
def par_o_impar(numero):
    """
    Recibe un número entero y devuelve "par" o "impar".
    Maneja también números negativos y cero.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Prueba:
# print(par_o_impar(-4)) # par
# print(par_o_impar(7))  # impar


# -------------------------------------------------------
# 2. Año bisiesto
# -------------------------------------------------------
def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    Regla: divisible por 4, pero no por 100, salvo que sea divisible por 400.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return "Es bisiesto"
    else:
        return "No es bisiesto"

# Prueba:
# print(es_bisiesto(2000)) # Es bisiesto (divisible por 400)
# print(es_bisiesto(1900)) # No es bisiesto (divisible por 100 pero no por 400)
# print(es_bisiesto(2024)) # Es bisiesto


# -------------------------------------------------------
# 3. Mayor de tres
# -------------------------------------------------------
def mayor_de_tres(lista):
    """
    Dada una lista de tres números, devuelve el mayor.
    Si hay empates, indica cuántos valores son iguales al máximo.
    """
    # Encontramos el valor máximo usando la función max()
    valor_maximo = max(lista)
    
    # Contamos cuántas veces aparece ese máximo en la lista
    cantidad_maximos = lista.count(valor_maximo)
    
    mensaje = f"El mayor número es {valor_maximo}. "
    if cantidad_maximos > 1:
        mensaje += f"Hay {cantidad_maximos} valores iguales al máximo."
    else:
        mensaje += "Es único."
        
    return mensaje

# Prueba:
# print(mayor_de_tres([10, 5, 10])) # El mayor es 10. Hay 2 valores iguales al máximo.
# print(mayor_de_tres([1, 2, 3]))   # El mayor es 3. Es único.


# -------------------------------------------------------
# 4. Clasificador de edad
# -------------------------------------------------------
def clasificar_edad(edad):
    """
    Recibe una edad y devuelve la categoría:
    infante, niño, adolescente, adulto, senior.
    """
    if edad >= 0 and edad <= 2:
        return "Infante"
    elif edad >= 3 and edad <= 12:
        return "Niño"
    elif edad >= 13 and edad <= 17:
        return "Adolescente"
    elif edad >= 18 and edad <= 64:
        return "Adulto"
    elif edad >= 65:
        return "Senior"
    else:
        return "Edad no válida (negativa)"

# Prueba:
# print(clasificar_edad(1))   # Infante
# print(clasificar_edad(15))  # Adolescente
# print(clasificar_edad(70))  # Senior


# -------------------------------------------------------
# 5. Descuentos por compra
# -------------------------------------------------------
def calcular_precio_con_descuento(precio):
    """
    Aplica descuentos:
    - 10% si supera $100
    - 5% si supera $50
    - Ninguno en caso contrario
    Devuelve el precio final con dos decimales.
    """
    precio_final = 0.0
    
    if precio > 100:
        precio_final = precio * 0.90  # 10% de descuento
    elif precio > 50:
        precio_final = precio * 0.95  # 5% de descuento
    else:
        precio_final = precio         # Sin descuento
        
    # Retornamos formateado a 2 decimales
    return f"${precio_final:.2f}"

# Prueba:
# print(calcular_precio_con_descuento(120)) # $108.00
# print(calcular_precio_con_descuento(60))  # $57.00
# print(calcular_precio_con_descuento(30))  # $30.00


# --- BLOQUE DE PRUEBAS RÁPIDAS ---
if __name__ == "__main__":
    print(f"El número -4 es: {par_o_impar(-4)}")
    print(f"El año 2000: {es_bisiesto(2000)}")
    print(f"Lista [5, 9, 5]: {mayor_de_tres([5, 9, 5])}")
    print(f"Edad 16: {clasificar_edad(16)}")
    print(f"Compra de $120: {calcular_precio_con_descuento(120)}")
    # ==========================================
# BLOQUE 2: CICLOS (FOR / WHILE)
# ==========================================

# -------------------------------------------------------
# 6. Suma de números pares
# -------------------------------------------------------
def suma_pares_for(n):
    """Calcula la suma de pares entre 1 y N usando un ciclo FOR."""
    suma = 0
    # range(inicio, fin_exclusivo, paso)
    # Empezamos en 2, vamos hasta N+1, de 2 en 2
    for i in range(2, n + 1, 2):
        suma += i
    return suma

def suma_pares_while(n):
    """Calcula la suma de pares entre 1 y N usando un ciclo WHILE."""
    suma = 0
    i = 2
    while i <= n:
        suma += i
        i += 2
    return suma

# Prueba:
# print(f"Suma pares (FOR) hasta 10: {suma_pares_for(10)}")  # 2+4+6+8+10 = 30
# print(f"Suma pares (WHILE) hasta 10: {suma_pares_while(10)}")


# -------------------------------------------------------
# 7. Factorial
# -------------------------------------------------------
def calcular_factorial(n):
    """
    Calcula el factorial de un número entero positivo (n!).
    Nota: En Python, los integers pueden ser muy grandes, así que el 
    'overflow' no es un error como en otros lenguajes, pero simularemos
    una validación básica de entrada.
    """
    if n < 0:
        return "Error: No existe factorial de números negativos."
    
    factorial = 1
    if n == 0:
        return 1
    
    for i in range(1, n + 1):
        factorial *= i
        
    return factorial

# Prueba:
# print(f"Factorial de 5: {calcular_factorial(5)}") # 120
# print(f"Factorial de 0: {calcular_factorial(0)}") # 1


# -------------------------------------------------------
# 8. Secuencia de Fibonacci
# -------------------------------------------------------
def fibonacci(n_terminos):
    """
    Genera los primeros N términos de la serie de Fibonacci.
    Imprime cada término en una línea separada.
    """
    # Inicializamos los dos primeros números
    a, b = 0, 1
    
    print(f"Serie de Fibonacci ({n_terminos} términos):")
    for _ in range(n_terminos):
        print(a)
        # Actualizamos los valores: a toma el valor de b, y b toma la suma de a+b
        a, b = b, a + b

# Prueba:
# fibonacci(7) # 0, 1, 1, 2, 3, 5, 8


# -------------------------------------------------------
# 9. Número primo (Optimizado)
# -------------------------------------------------------
import math

def es_primo(numero):
    """
    Determina si un número es primo.
    Optimización: Solo verificamos hasta la raíz cuadrada del número.
    """
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    
    # Verificamos desde 3 hasta la raíz cuadrada, saltando de 2 en 2 (solo impares)
    limite = int(math.sqrt(numero)) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
            
    return True

# Prueba:
# print(f"¿Es 17 primo? {es_primo(17)}") # True
# print(f"¿Es 49 primo? {es_primo(49)}") # False


# -------------------------------------------------------
# 10. Patrón de asteriscos
# -------------------------------------------------------
def triangulo_asteriscos(n):
    """Imprime un triángulo rectángulo de altura N."""
    print(f"\nTriángulo de altura {n}:")
    for i in range(1, n + 1):
        # En Python, multiplicar un string por un número lo repite
        print("*" * i)

def triangulo_invertido(n):
    """Variante: Imprime el triángulo invertido."""
    print(f"\nTriángulo invertido de altura {n}:")
    for i in range(n, 0, -1): # Range inverso
        print("*" * i)

# Prueba:
# triangulo_asteriscos(5)
# triangulo_invertido(5)


# --- BLOQUE DE PRUEBAS RÁPIDAS ---
if __name__ == "__main__":
    print("--- Probando Ciclos ---")
    print(f"Suma pares (hasta 10): {suma_pares_for(10)}")
    print(f"Factorial de 6: {calcular_factorial(6)}")
    fibonacci(5)
    print(f"¿Es 13 primo? {es_primo(13)}")
    triangulo_asteriscos(3)
    # ==========================================
# BLOQUE 3: FUNCIONES REUTILIZABLES
# ==========================================

import random
import string

# -------------------------------------------------------
# 11. Conversor de unidades
# -------------------------------------------------------
def convertir_unidades(valor, modo="m2ft"):
    """
    Convierte metros a pies o viceversa.
    modo "m2ft": Metros a Pies.
    modo "ft2m": Pies a Metros.
    """
    if modo == "m2ft":
        return valor * 3.28084
    elif modo == "ft2m":
        return valor / 3.28084
    else:
        return "Modo no válido. Use 'm2ft' o 'ft2m'."

# Prueba:
# print(f"10 metros a pies: {convertir_unidades(10)}")
# print(f"32 pies a metros: {convertir_unidades(32, 'ft2m')}")


# -------------------------------------------------------
# 12. Validador de contraseñas
# -------------------------------------------------------
def validar_contrasena(password):
    """
    Verifica que tenga al menos 8 caracteres, mayúscula, minúscula y dígito.
    Devuelve una lista de errores. Si está vacía, la contraseña es válida.
    """
    errores = []
    
    if len(password) < 8:
        errores.append("Falta longitud (mínimo 8 caracteres)")
    
    # Verificamos usando flag (banderas)
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    
    for char in password:
        if char.isupper(): tiene_mayuscula = True
        if char.islower(): tiene_minuscula = True
        if char.isdigit(): tiene_digito = True
            
    if not tiene_mayuscula:
        errores.append("Falta una letra mayúscula")
    if not tiene_minuscula:
        errores.append("Falta una letra minúscula")
    if not tiene_digito:
        errores.append("Falta un número (dígito)")
        
    return errores

# Prueba:
# errores = validar_contrasena("abc1")
# print(errores) # ['Falta longitud...', 'Falta mayúscula']


# -------------------------------------------------------
# 13. Ordenamiento burbuja (Bubble Sort)
# -------------------------------------------------------
def ordenamiento_burbuja(lista, ascendente=True):
    """
    Implementa el algoritmo burbuja.
    ascendente=True: Ordena de menor a mayor.
    ascendente=False: Ordena de mayor a menor.
    Modifica la lista original y también la retorna.
    """
    n = len(lista)
    # Recorremos la lista n veces
    for i in range(n):
        # Recorremos la lista hasta n-i-1 para no comparar lo ya ordenado
        for j in range(0, n - i - 1):
            
            # Lógica condicional para decidir si intercambiamos
            debe_intercambiar = False
            
            if ascendente:
                if lista[j] > lista[j+1]:
                    debe_intercambiar = True
            else:
                if lista[j] < lista[j+1]:
                    debe_intercambiar = True
            
            # Intercambio (swap) usando tuple unpacking de Python
            if debe_intercambiar:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    return lista

# Prueba:
# nums = [64, 34, 25, 12, 22, 11, 90]
# print(f"Original: {nums}")
# print(f"Descendente: {ordenamiento_burbuja(nums.copy(), ascendente=False)}")


# -------------------------------------------------------
# 14. Calculadora de IMC
# -------------------------------------------------------
def calcular_imc(peso_kg, altura_m):
    """
    Calcula el Índice de Masa Corporal y su categoría.
    Redondea a dos decimales.
    """
    if altura_m <= 0:
        return "Error: La altura debe ser positiva."

    imc = peso_kg / (altura_m ** 2)
    imc_redondeado = round(imc, 2)
    
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
        
    return imc_redondeado, categoria

# Prueba:
# valor, cat = calcular_imc(70, 1.75)
# print(f"IMC: {valor} - Categoría: {cat}")


# -------------------------------------------------------
# 15. Generador de contraseñas
# -------------------------------------------------------
def generar_contrasena(longitud=12, usar_simbolos=True, usar_numeros=True):
    """
    Genera una contraseña aleatoria.
    Garantiza al menos un carácter de cada tipo solicitado.
    """
    # Definimos los conjuntos de caracteres
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation
    
    # El pool base siempre tiene letras (mayus y minus)
    pool = letras_minusculas + letras_mayusculas
    
    caracteres_obligatorios = [
        random.choice(letras_minusculas),
        random.choice(letras_mayusculas)
    ]
    
    if usar_numeros:
        pool += digitos
        caracteres_obligatorios.append(random.choice(digitos))
        
    if usar_simbolos:
        pool += simbolos
        caracteres_obligatorios.append(random.choice(simbolos))
        
    # Si la longitud pedida es menor que la cantidad de caracteres obligatorios,
    # ajustamos la longitud para evitar errores
    if longitud < len(caracteres_obligatorios):
        longitud = len(caracteres_obligatorios)
    
    # Llenamos el resto de la contraseña aleatoriamente desde el pool
    longitud_restante = longitud - len(caracteres_obligatorios)
    resto_caracteres = [random.choice(pool) for _ in range(longitud_restante)]
    
    # Combinamos lista obligatoria + lista resto
    contrasena_lista = caracteres_obligatorios + resto_caracteres
    
    # Mezclamos (shuffle) para que los obligatorios no siempre estén al principio
    random.shuffle(contrasena_lista)
    
    # Unimos la lista en un string
    return "".join(contrasena_lista)

# Prueba:
# print(generar_contrasena(longitud=10, usar_simbolos=False))


# --- BLOQUE DE PRUEBAS RÁPIDAS ---
if __name__ == "__main__":
    print("--- Probando Funciones Reutilizables ---")
    
    # 11
    print(f"5 metros a pies: {convertir_unidades(5, 'm2ft'):.2f}")
    
    # 12
    err = validar_contrasena("Hola123")
    print(f"Errores 'Hola123': {err}") # Debería estar vacío o lista vacía
    
    # 13
    lista_nums = [3, 1, 4, 1, 5, 9]
    print(f"Lista ordenada: {ordenamiento_burbuja(lista_nums)}")
    
    # 14
    imc_val, cat = calcular_imc(80, 1.80)
    print(f"IMC: {imc_val} ({cat})")
    
    # 15
    print(f"Contraseña generada: {generar_contrasena(12)}")
    # ==========================================
# BLOQUE 4: COMBINACIÓN (CONDICIONALES, CICLOS, FUNCIONES)
# ==========================================

import random
import calendar

# -------------------------------------------------------
# 16. Juego de adivinar número
# -------------------------------------------------------
def juego_adivinar_numero():
    """
    El programa elige un número entre 1 y 100.
    El usuario tiene 10 intentos para adivinarlo.
    """
    print("--- Juego: Adivina el Número ---")
    secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    adivinado = False
    
    while intentos < max_intentos and not adivinado:
        try:
            entrada = int(input(f"Intento {intentos + 1}/{max_intentos}. Ingresa un número (1-100): "))
            
            if entrada < 1 or entrada > 100:
                print("Por favor, ingresa un número dentro del rango 1-100.")
                continue
            
            intentos += 1
            
            if entrada == secreto:
                print(f"¡Felicidades! Has ganado en {intentos} intentos. El número era {secreto}.")
                adivinado = True
            elif entrada < secreto:
                print("El número secreto es MAYOR.")
            else:
                print("El número secreto es MENOR.")
                
        except ValueError:
            print("Error: Debes ingresar un número entero.")
            
    if not adivinado:
        print(f"Fin del juego. Se acabaron los intentos. El número era {secreto}.")

# Para probar, descomenta: juego_adivinar_numero()


# -------------------------------------------------------
# 17. Tablas de multiplicar
# -------------------------------------------------------
def tabla_multiplicar(n):
    """Muestra la tabla de multiplicar del número N."""
    print(f"\n--- Tabla del {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def todas_las_tablas():
    """Imprime todas las tablas del 1 al 10."""
    for i in range(1, 11):
        tabla_multiplicar(i)

# Para probar una tabla: tabla_multiplicar(5)
# Para probar todas: todas_las_tablas()


# -------------------------------------------------------
# 18. Análisis de texto
# -------------------------------------------------------
def analizar_texto(texto):
    """
    Cuenta vocales, consonantes y espacios.
    Ignora mayúsculas/minúsculas y signos de puntuación.
    """
    vocales = "aeiouáéíóú"
    conteo_vocales = 0
    conteo_consonantes = 0
    conteo_espacios = 0
    
    # Convertimos a minúsculas para facilitar la comparación
    texto_lower = texto.lower()
    
    for char in texto_lower:
        if char.isspace():
            conteo_espacios += 1
        elif char.isalpha(): # isalpha verifica si es una letra (ignora números y signos)
            if char in vocales:
                conteo_vocales += 1
            else:
                conteo_consonantes += 1
                
    return {
        "vocales": conteo_vocales,
        "consonantes": conteo_consonantes,
        "espacios": conteo_espacios
    }

# Prueba:
# resultado = analizar_texto("Hola Mundo 123!")
# print(resultado)


# -------------------------------------------------------
# 19. Simulador de cajero automático
# -------------------------------------------------------
def simulador_cajero():
    """
    Menú interactivo: consultar, depositar, retirar, salir.
    Límite de retiro diario: $500.
    """
    saldo = 1000.00  # Saldo inicial
    retiro_diario = 0.00
    limite_diario = 500.00
    
    print(f"\n--- Cajero Automático ---")
    print(f"Saldo inicial: ${saldo:.2f}")
    
    while True:
        print("\n1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            print(f"Tu saldo actual es: ${saldo:.2f}")
            
        elif opcion == "2":
            try:
                monto = float(input("Ingresa el monto a depositar: "))
                if monto > 0:
                    saldo += monto
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("El monto debe ser positivo.")
            except ValueError:
                print("Error: Ingresa un número válido.")
                
        elif opcion == "3":
            try:
                monto = float(input("Ingresa el monto a retirar: "))
                
                if monto <= 0:
                    print("El monto debe ser positivo.")
                elif monto > saldo:
                    print("Error: Saldo insuficiente.")
                elif (retiro_diario + monto) > limite_diario:
                    disponible = limite_diario - retiro_diario
                    print(f"Error: Superas el límite diario de retiro (${limite_diario}).")
                    print(f"Solo puedes retirar ${disponible:.2f} más hoy.")
                else:
                    saldo -= monto
                    retiro_diario += monto
                    print(f"Retiro exitoso. Retirado hoy: ${retiro_diario:.2f}")
                    print(f"Saldo restante: ${saldo:.2f}")
                    
            except ValueError:
                print("Error: Ingresa un número válido.")
                
        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Adiós!")
            break
            
        else:
            print("Opción no válida. Intenta de nuevo.")

# Para probar, descomenta: simulador_cajero()


# -------------------------------------------------------
# 20. Calendario mensual
# -------------------------------------------------------
def mostrar_calendario(mes, anio):
    """
    Muestra el calendario del mes y año dados.
    Utiliza la biblioteca estándar 'calendar'.
    """
    # Validación básica
    if mes < 1 or mes > 12:
        print("Error: El mes debe estar entre 1 y 12.")
        return

    # calendar.month() devuelve una cadena formateada del calendario
    cal_texto = calendar.month(anio, mes)
    print(cal_texto)

# Prueba:
# mostrar_calendario(10, 2023) # Muestra octubre de 2023