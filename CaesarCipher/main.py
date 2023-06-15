"""
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 * Info: https://en.wikipedia.org/wiki/Caesar_cipher
"""

def invert_alphabet(alphabet):
    inverted_alphabet = {}
    for key, value in alphabet.items():
        inverted_alphabet[value] = key
    return inverted_alphabet


def caesar_cipher(text, step, direction, alphabet):
    if direction != 'right' and direction != 'left':
        return "ERROR: Direction value is incorrect. It must be 'right' or 'left'"
    
    text = text.upper()
    inverted_alphabet = invert_alphabet(alphabet)
    
    result = ""
    for char in text:
        if char in alphabet:
            if direction == 'right':
                cal_step = alphabet[char] + step
            else:
                cal_step = alphabet[char] - step
                
            result += inverted_alphabet[cal_step % 26]
        else:
            result += char

    return result


def main():
    alphabet = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 
        'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 
        'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 
        'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }

    print(caesar_cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 3, 'right', alphabet))
    print(caesar_cipher("WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ", 3, 'left', alphabet))
    print(caesar_cipher("I LOVE CAESAR ENCRYPTION", 8, 'right', alphabet))
    print(caesar_cipher("Q TWDM KIMAIZ MVKZGXBQWV", 8, 'left', alphabet))
    print(caesar_cipher("HELLO, HOW ARE YOU?", 16, 'left', alphabet))
    print(caesar_cipher("ROVVY, RYG KBO IYE?", 16, 'right', alphabet))
    print(caesar_cipher("THIS IS A TEST", 54, 'left', alphabet))
    print(caesar_cipher("RFGQ GQ Y RCQR", 54, 'right', alphabet))


if __name__ == "__main__":
    main()