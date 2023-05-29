"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
"""
import re

def text_analyzer(text):
    word_count = 0
    sentence_count = 0
    word_lenghts = []
    max_length = 0
    largest_words = []
    
    current_word = ''
    current_word_length = 0
    text = re.sub('[!"#$%&\'()*+,\-/:;<=>?@[\]^_`{|}~]', '', text)
    text = text.replace('\n', ' ')
    
    for char in text:
        end_word = False
        if char == ' ':
            if current_word != '':
                word_count += 1
                end_word = True
        elif char == '.':
            if current_word != '':
                word_count += 1
                sentence_count += 1
                end_word = True
        else:
            current_word += char
            current_word_length += 1

        if end_word:
            word_lenghts.append(current_word_length)
            if current_word_length > max_length:
                max_length = current_word_length
                largest_words.clear()
                largest_words.append(current_word)
            elif current_word_length == max_length:
                largest_words.append(current_word)

            current_word = ''
            current_word_length = 0
    
    return {
        "Número de palabras": word_count,
        "Longitud media de palabras": (sum(word_lenghts) / word_count),
        "Número de oraciones": sentence_count,
        "Palabra/s más largas": largest_words
    }


def main():
    print(text_analyzer("""
Nos encontramos en un
periodo de guerra civil. Las
naves espaciales rebeldes,
atacando desde una base
oculta, han logrado su 
primera victoria contra
el malvado Imperio
Galáctico.

Durante la batalla, los 
espías rebeldes han
conseguido apoderarse de 
los planos secretos del
arma total y definitiva del
Imperio, la ESTRELLA
DE LA MUERTE,
una estación espacial
acorazada, llevando en sí
potencia suficiente para
destruir a un planeta
entero.

Perseguida por los 
siniestros agentes del 
Imperio, la Princesa Leia 
vuela hacia su patria, a
bordo de su nave espacial,
llevando consigo los
planos robados, que
pueden salvar a su pueblo
y devolver la libertad a la
galaxia....
"""))


if __name__ == "__main__":
    main()