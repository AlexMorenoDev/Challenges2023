"""
 * Crea una función que sea capaz de transformar el inglés al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
"""


def aurebesh_to_english(text, alphabet):
    result = ""
    text = text.lower()

    text_length = len(text)
    i = 0
    while i < text_length:
        current_char = text[i]
        next_char = None
        if i != (text_length-1):
            next_char = text[i+1]
            
        if next_char and (current_char + next_char) in alphabet:
            result += alphabet[current_char + next_char]
            i += 1
        elif current_char in alphabet:
            result += alphabet[current_char]
        else:
            result += current_char
        
        i += 1
    
    return result


def english_to_aurebesh(text, alphabet):
    result = ""
    text = text.lower()

    aurebesh_letter = ""
    alphabet_values = set(alphabet.values())
    for char in text:
        if char in alphabet_values:
            aurebesh_letter += char
            if aurebesh_letter in alphabet:
                result += alphabet[aurebesh_letter]
                aurebesh_letter = ""
        else:
            result += char

    return result


def main():
    aurebesh_alphabet = {
        'a': "aurek", 'b': "besh", 'c': "cresh", 'd': "dorn",
        'e': "esk", 'f': "forn", 'g': "grek", 'h': "herf",
        'i': "isk", 'j': "jenth", 'k': "krill", 'l': "leth",
        'm': "mern", 'n': "nerm", 'o': "osk", 'p': "peth",
        'q': "qek", 'r': "resh", 's': "senth", 't': "trill",
        'u': "usk", 'v': "vev", 'w': "wesk", 'x': "xesh",
        'y': "yirt", 'z': "zerek", 'ch': "cherek", 'ae': "enth",
        'eo': "onith", 'kh': "krenth", 'ng': "nen", 'oo': "orenth",
        'sh': "shen", 'th': "thesh"
    }

    aurebesh_alphabet_inverted = {}
    for key, value in aurebesh_alphabet.items():
        aurebesh_alphabet_inverted[value] = key

    print(aurebesh_to_english("Hello", aurebesh_alphabet))
    print(english_to_aurebesh("herfesklethlethosk", aurebesh_alphabet_inverted))
    print(aurebesh_to_english("What do you think about this?", aurebesh_alphabet))
    print(english_to_aurebesh("weskherfaurektrill dornosk yirtoskusk theshisknermkrill aurekbeshoskusktrill theshisksenth?", aurebesh_alphabet_inverted))

if __name__ == "__main__":
    main()