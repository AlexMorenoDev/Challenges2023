"""
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
"""
import time

def is_integer(n):
    return isinstance(n, int)

# n_start: countdown initial point/number
# s_between: seconds between countdown update
def countdown(n_start, s_between):
    if n_start > 0 and s_between > 0 and is_integer(n_start) and is_integer(s_between):
        print(n_start)
        while n_start > 0:
            time.sleep(s_between)
            n_start -= 1 
            print(n_start)
        print("Countdown finished!")
    else:
        raise Exception("ERROR: Both paremeters must be positive integer numbers greater than 0!")


def main():
    countdown(10, 1)
    countdown(5, 5)


if __name__ == "__main__":
    main()