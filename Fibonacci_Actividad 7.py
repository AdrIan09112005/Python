import time

# Fibonacci
def fibonacci_1(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibonacci_1 (n-1) + fibonacci_1 (n-2)
        
numerito_2 = 5
inicio = time.time()
print(f"La serie de Fibonacci hasta {numerito_2} numero es {fibonacci_1(numerito_2)}")
fin = time.time()
print(f"El tiempo de ejecución es: {fin-inicio} s")


# Fibonacci sin recursividad
def fibonacci_2(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

numerito_3 = 20
inicio = time.time()
print(f"La serie de Fibonacci hasta {numerito_3} numero es {fibonacci_2(numerito_3)}")
fin = time.time()
print(f"El tiempo de ejecución es: {fin-inicio} s")
