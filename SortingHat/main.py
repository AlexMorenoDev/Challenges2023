"""
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""

import re
import random

def ask_input_to_user(answers):
    user_answer = None
    
    while True:
        try:
            user_answer = int(input("Introduce tu respuesta (1-4):\n"))
            break
        except:
            print("ERROR: Solo se puede introducir un número del 1 al 4")

    return answers[user_answer]

def get_selected_house(target_dict):
    max_val = 0
    max_keys = []
    for key, value in target_dict.items():
        if value > max_val:
            max_val = value
            max_keys.clear()
            max_keys.append(key)
        elif value == max_val:
            max_keys.append(key)

    return random.choice(max_keys)

def main():
    pattern = r"^\d+\."
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    count = 0
    answers = {}
    with open('questions.txt', 'r') as textfile:
        for line in textfile:
            if line != "\n":
                parts = line.rstrip().split('|')
                print(parts[0])
                if re.search(pattern, line):
                    count += 1
                    answers[count] = parts[1]
            else:
                houses[ask_input_to_user(answers)] += 1
                count = 0
                answers = {}
    
    if count > 0:
        houses[ask_input_to_user(answers)] += 1

    print("\nResultado final:")
    print(get_selected_house(houses) + "!!!!")

if __name__ == "__main__":
    main()