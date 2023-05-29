"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 """

def initialize_alphabet(txt_path):
    leet_alphabet = {}
    with open(txt_path, 'r') as txt_file:
        for line in txt_file:
            parts = line.rstrip().split(' ')
            leet_alphabet[parts[0]] = parts[1]

    return leet_alphabet


def text_to_leet_encoder(leet_alphabet, text):
    converted_text = ""

    for c in text:
        try:
            converted_text += leet_alphabet[c.lower()]
        except KeyError:
            converted_text += c

    return converted_text


def main():
    text = "leet"
    leet_alphabet = initialize_alphabet("LeetAlphabet.txt")
    converted_text = text_to_leet_encoder(leet_alphabet, text)
    print(converted_text)
    

if __name__ == "__main__":
    main()