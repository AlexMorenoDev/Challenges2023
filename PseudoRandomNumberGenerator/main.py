"""
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
"""
import time

# Linear congruential generator
def custom_random():
    # (a * X + c) mod m --> We add '% 101' because we are searching for a number between 0 and 100
    return ((1103515245 * time.time_ns() + 12345) % (2**31)) % 101


def main():
    print(custom_random())


if __name__ == "__main__":
    main()

