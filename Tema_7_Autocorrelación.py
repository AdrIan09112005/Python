"""Recursividad"""
import time
# Factorial sin Recursividad
def factorial_1(n): 
    tamal = 1
    for i in range (2, n + 1):
        tamal = tamal * i
    return tamal

# Ejemplo de Uso
numerito = 5
inicio = time.time()
print(f"El factorial de {numerito} es {factorial_1(numerito)}")
fin = time.time()
print(f"El tiempo de ejecución es: {fin-inicio} s")

#Interupcción por Teclado Ctrl C

# Factorial con Recursividad
def factorial_2(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial_2(n-1)

# Ejemplo de Uso
numerito_1 = 100
inicio = time.time()
print(f"El factorial de {numerito_1} es {factorial_2(numerito_1)}")
fin = time.time()
print(f"El tiempo de ejecución es: {fin-inicio} s")