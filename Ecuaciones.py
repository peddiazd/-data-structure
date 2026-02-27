# SISTEMA 3x3 - METODO DE REDUCCION
print("RESOLUCION DE SISTEMA 3x3 POR METODO DE REDUCCION")
print("Forma general: ax + by + cz = d")
print("Ingrese los coeficientes de cada ecuación")
print("---------------------------------------------")
# ==========================================================
# FUNCIÓN PARA FORMATEAR LOS TÉRMINOS CON SIGNOS CORRECTOS
# ------------------------------------------------------------
# Esta función sirve únicamente para mostrar la ecuación
# respetando la ley de signos (no mostrar + - , sino - directamente)

def formatear_termino(coef, variable):
    if coef == 0:
        return ""
    if coef == 1:
        return f"+ {variable}"
    if coef == -1:
        return f"- {variable}"
    if coef > 0:
        return f"+ {coef}{variable}"
    else:
        return f"- {abs(coef)}{variable}"


# ------------------------------------------------------------
# INGRESO DE DATOS
# ------------------------------------------------------------
# Se piden los coeficientes de cada ecuación.
# Forma general:
# ax + by + cz = d

print("Ingrese los coeficientes de la primera ecuación")
a1 = float(input("Coeficiente de x: "))  # coeficiente de x en ecuación 1
b1 = float(input("Coeficiente de y: "))  # coeficiente de y en ecuación 1
c1 = float(input("Coeficiente de z: "))  # coeficiente de z en ecuación 1
d1 = float(input("Resultado: "))         # término independiente

print("\nIngrese los coeficientes de la segunda ecuación")
a2 = float(input("Coeficiente de x: "))
b2 = float(input("Coeficiente de y: "))
c2 = float(input("Coeficiente de z: "))
d2 = float(input("Resultado: "))

print("\nIngrese los coeficientes de la tercera ecuación")
a3 = float(input("Coeficiente de x: "))
b3 = float(input("Coeficiente de y: "))
c3 = float(input("Coeficiente de z: "))
d3 = float(input("Resultado: "))


# ------------------------------------------------------------
# MOSTRAR EL SISTEMA INGRESADO
# ------------------------------------------------------------

print("\nSistema ingresado:")

def mostrar_ecuacion(a,b,c,d):
    texto = ""
    if a != 0:
        if a == 1:
            texto += "x "
        elif a == -1:
            texto += "-x "
        else:
            texto += f"{a}x "
    texto += formatear_termino(b,"y") + " "
    texto += formatear_termino(c,"z")
    print(texto.replace("+ -","- "), "=", d)

mostrar_ecuacion(a1,b1,c1,d1)
mostrar_ecuacion(a2,b2,c2,d2)
mostrar_ecuacion(a3,b3,c3,d3)


# ============================================================
# MÉTODO DE ELIMINACIÓN
# ============================================================
# Paso 1: Eliminamos la variable z
# Para hacerlo:
# Multiplicamos ecuaciones para que los coeficientes de z
# queden opuestos y se cancelen al restar.


# -------- ELIMINACIÓN DE z ENTRE ECUACIÓN 1 Y 2 --------

m1 = c2   # multiplicador de ecuación 1
m2 = c1   # multiplicador de ecuación 2

# Nuevos coeficientes después de restar las ecuaciones
A1 = a1*m1 - a2*m2
B1 = b1*m1 - b2*m2
D1 = d1*m1 - d2*m2


# -------- ELIMINACIÓN DE z ENTRE ECUACIÓN 1 Y 3 --------

m3 = c3
m4 = c1

A2 = a1*m3 - a3*m4
B2 = b1*m3 - b3*m4
D2 = d1*m3 - d3*m4


# Ahora tenemos un sistema 2x2:
# A1x + B1y = D1
# A2x + B2y = D2


# -------- ELIMINACIÓN DE y --------

m5 = B2
m6 = B1

Ax = A1*m5 - A2*m6
Dx = D1*m5 - D2*m6

# Resolviendo para x
x = Dx / Ax


# -------- ENCONTRAR y --------
# Sustituimos el valor de x en una de las ecuaciones 2x2

y = (D1 - A1*x) / B1


# -------- ENCONTRAR z --------
# Sustituimos x e y en la primera ecuación original

z = (d1 - a1*x - b1*y) / c1


# ------------------------------------------------------------
# RESULTADO FINAL
# ------------------------------------------------------------

print("\nSolución del sistema:")
print("x =", round(x,4))
print("y =", round(y,4))
print("z =", round(z,4))


# ============================================================
# COMPROBACIÓN
# ============================================================
# Se sustituyen los valores encontrados en las ecuaciones
# originales para verificar que la igualdad se cumple.

print("\nComprobación:")

ver1 = a1*x + b1*y + c1*z
print("Ecuación 1:", round(ver1,4), "=", d1)

ver2 = a2*x + b2*y + c2*z
print("Ecuación 2:", round(ver2,4), "=", d2)

ver3 = a3*x + b3*y + c3*z
print("Ecuación 3:", round(ver3,4), "=", d3)