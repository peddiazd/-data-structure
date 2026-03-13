#definir funcion 
def saludar ():
    #Vamos a saludar
    """ Vamos a saludar"""
    print("Hola perras ")
saludar()

#definir una funcionn con parametros donde me pregunte nombre y edad  

def saluda_persona(nombre, edad):
    """Saludar a una persona y pide el nombre (str)y edad (int)"""
    print(f"Hola {nombre}. tienes {edad} años")
saluda_persona("Assael",20)


#calcular el area de un rectangulo 

def calcula_area_rectangulo(base:float,altura:float)->float:
    """calcula el area de un rectangulo y returna con float"""
    area=base*altura
    return area
resultado = calcula_area_rectangulo(5,6)
print(f"El area del rectangulo es : {resultado}")

#calcular potencia 
def calcular_potencia(base,exponente=2):
    """Calcula base elevado a exponente, sino se especifica exponente , calcula el cuadrado"""
    resultado = base**exponente
    return resultado
print(calcular_potencia(4))
print(calcular_potencia(3,4))
print(calcular_potencia(2,5))


#retorno de multiples de valores
def calcular_estadisticas(numeros):
    """Calcula y retorna suma,promedio y maximo de una lista """
    total=sum(numeros)
    promedio=total/len(numeros)
    maximo=max(numeros)
    return total,promedio,maximo
#desempaquetado de la tupla
notas=[47,44,55,43,96]
suma,avg,max = calcular_estadisticas(notas)

print(f"La suma es : {suma}")
print(f"el promedio es : {avg}")
print(f"El maximo es : {max}")


#variables locales

def variable_local():
    x = 10 #variable local
    print(x)
variable_local()

#variable globla 
s = "Somos fuertes"
def mostrar():
    print(s)
mostrar()


def factorial(n):
    """Calcula el factorial de n de forma recursiva.
     parametros: n (int)- numero entero no negativo
     retorna: int - el factorial de n """
    if n == 0 or n==1 :
        return 1
    else :
        return n *factorial(n-1)
    
    
    
        
    


    


