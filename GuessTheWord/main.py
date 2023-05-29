'''
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
'''
from classes.word import Word

def main():
    target_word = Word()
    r = 1
    guess = None
    attempts = 10
    typed_letters = []
    input("Welcome to 'Guess the word' game! Press 'Enter' to start...")
    while guess != target_word.text and attempts > 0:
        if guess != "":
            print("Round " + str(r))
            target_word.show_incomplete()
            print("Attempts left: " + str(attempts))
            print("Typed letters: " + str(typed_letters))
        
        guess = input("Type a letter or type the entire word if you already know it: ")
        
        if guess == "":
            continue
        if len(guess) > 1:
            if guess != target_word.text:
                print("Wrong answer! Try again!")
            else:
                break
        else:
            if guess in target_word.hidden_chars:
                print("Correct letter!")
                target_word.update_incomplete_word(guess)
            else:
                print("Incorrect letter! Try again!")
                if guess not in typed_letters:
                    typed_letters.append(guess)
        
        attempts -= 1
        r += 1
        
        print("----------------------------")

    if attempts > 0:
        print("Congratulations! You won, the word was '" + target_word.text + "'. :)")
        print("Attempts left: " + str(attempts))
    else:
        print("Sorry! You lost. Good luck next time. :(")
        
    
if __name__ == "__main__":
    main()