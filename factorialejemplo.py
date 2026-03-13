def factorial(n):
    """Calcula el factorial de n de forma recursiva.
     parametros: n (int)- numero entero no negativo
     retorna: int - el factorial de n """
    if n == 0 or n==1 :
        return 1
    else :
        return n *factorial(n-1)


#print
n = int(input("Digita el factorial : "))
print(factorial(n))
