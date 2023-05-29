"""
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
"""

def add_prefix(n, base, prefixes):
    return prefixes[base] + n


# Converts a decimal number to octal or hexadecimal
# 3 parameters:
#   - n: decimal number
#   - base: 8 (octal) or 16 (hexadecimal)
#   - hex_dict: hexadecimal values for 10,...,15 --> 10: A,... 15: F
def decimal_converter(n, base, prefixes, hex_dict=None):
    if base != 8 and base != 16:
        return "ERROR: Incorrect base! It must be 8 or 16."
    if base == 16 and not hex_dict:
        return "ERROR: Hexadecimal dictionary is empty! If base is 16, hexadecimal dictionary must be entered as third parameter."
    if n == 0:
        return add_prefix(n, base, prefixes)

    remainders = ""
    while n != 0:
        r = n % base
        
        if r > 9:
            remainders += hex_dict[r]
        else:
            remainders += str(r)
            
        n = n // base
    
    return add_prefix(remainders[::-1], base, prefixes)


def main():
    hex_dict = {
        10: 'A', 11: 'B',
        12: 'C', 13: 'D',
        14: 'E', 15: 'F'
    }
    prefixes = {8: "0o", 16: "0x"}

    print(decimal_converter(3432, 8, prefixes))
    print(decimal_converter(7562, 8, prefixes))
    print(decimal_converter(35631, 8, prefixes))
    print(decimal_converter(3432, 16, prefixes, hex_dict))
    print(decimal_converter(7562, 16, prefixes, hex_dict))
    print(decimal_converter(35631, 16, prefixes, hex_dict))


if __name__ == "__main__":
    main()