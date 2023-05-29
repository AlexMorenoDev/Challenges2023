"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
import sys

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def is_prime(n):
    for i in range(2, n):
        # If a remainder is 0, we can stop. (The number is not prime)
        if n % i == 0:
            return False
        # If the quotient is less than the divisor, we can stop. (The number is prime)
        if n / i < i:
            return True
    # If we get out of the loop the number is prime
    return True

def is_fibonacci(n):
    x = 0
    y = 1
    while True:
        if x == n:
            return True
        if x > n:
            return False

        new = x + y
        x = y
        y = new

def add_text(condition, text, print_message):
    if not condition:
        print_message += "not "
    print_message += text

    return print_message


def main():
    try:
        target = int(input("Enter a number: "))
    except:
        print("ERROR: You have to enter a valid number!")
        sys.exit()
    
    print_message = f"{target} is "

    if is_even(target):
        print_message += "even, "
    else:
        print_message += "odd, "
        
    print_message = add_text(is_prime(target), "prime and ", print_message)
    print_message = add_text(is_fibonacci(target), "fibonacci", print_message)
    
    print(print_message)

if __name__ == '__main__':
    main()