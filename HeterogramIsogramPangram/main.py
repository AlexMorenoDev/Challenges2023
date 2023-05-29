"""
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 */
"""
from string import ascii_lowercase as alphabet


def string_checker(string): 
    formatted_string = string.replace(" ", "").lower()
    alphabet_set = set(alphabet)
    for letter in formatted_string:
        if letter not in alphabet_set:
            return None
        
    return formatted_string


# https://en.wikipedia.org/wiki/Heterogram_(literature)
# A word, phrase, or sentence in which no letter of the alphabet occurs more than once
def is_heterogram(string):
    formatted_string = string_checker(string)
    if formatted_string:
        result = True
        letters_set = set()
        for char in formatted_string:
            if char not in letters_set:
                letters_set.add(char)
            else:
                result = False
                break

        return result
    return "ERROR: The input string contains characters that are not included in '" + alphabet + "'"
    

# https://en.wiktionary.org/wiki/isogram
# A word or phrase in which each letter occurs the same number of times.
def is_isogram(string):
    formatted_string = string_checker(string)
    if formatted_string:
        letters_dict = {}
        for char in formatted_string:
            if char not in letters_dict:
                letters_dict[char] = 1
            else:
                letters_dict[char] += 1
        
        result = True
        last = None
        for value in letters_dict.values():
            if last and last != value:
                result = False
                break
            last = value

        return result
    return "ERROR: The input string contains characters that are not included in '" + alphabet + "'"


# https://en.wikipedia.org/wiki/Pangram
# A word or phrase using every letter of a given alphabet at least once
def is_pangram(string):
    formatted_string = string_checker(string)
    if formatted_string:
        string_set = set(formatted_string)
        return len(string_set) == len(alphabet)
    return "ERROR: The input string contains characters that are not included in '" + alphabet + "'"


def main():
    print(is_heterogram(("dermatoglyphics")))
    print(is_heterogram("subdermatoglyphic"))
    print(is_heterogram("subderm#/atogl  yphic")) # Incorrect characters in string --> Error
    print(is_isogram("uncopyrightable"))
    print(is_pangram("The quick brown fox jumps over a lazy dog"))
    

if __name__ == "__main__":
    main()
