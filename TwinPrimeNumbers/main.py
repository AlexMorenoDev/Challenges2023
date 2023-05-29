"""
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
"""
from math import sqrt

# https://matematicasies.com/Averiguar-si-un-numero-es-primo
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        if n / i < i:
            return True
    return True

# Fastest way with higher values
def isPrime_2(n):
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False  
    return True


def show_twin_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n+1):
        #if isPrime(i):
        if isPrime_2(i):
            prime_numbers.append(i)
    
    result = []
    for i in range(len(prime_numbers)-1):
        current_num = prime_numbers[i]
        next_num = prime_numbers[i+1]
        if next_num - current_num == 2:
            result.append((current_num, next_num))
    
    print(result)


def main():
    show_twin_prime_numbers(14)
    show_twin_prime_numbers(30)
    show_twin_prime_numbers(100)
    show_twin_prime_numbers(1000)
    

if __name__ == "__main__":
    main()