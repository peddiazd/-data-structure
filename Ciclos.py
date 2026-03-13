#1 ejercicio




def factorial_recursivo(numero)-> int:
    if numero == 0 or numero ==1:
        return 1
    else:
        return numero*factorial_recursivo(numero-1)
print(factorial_recursivo(5))




def factWhile(nu)-> int:
    if nu == 0 or nu == 1:
        return 1
    while nu > 1 :
        return nu * factWhile(nu-1)
print(factWhile(5))


#fact for 
def factFor(nu2)-> int:
    acum =1
    for i in range(2,nu2+1):
        acum*=i
    return acum
print(factFor(5))






