"""
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 * https://en.wikipedia.org/wiki/Konami_Code
"""
import keyboard


def main():
    konami_code = ['↑', '↑', '↓', '↓', '←', '→', '←', '→', 'b', 'a']
    arrows = {"flecha arriba": '↑', "flecha abajo": '↓',
            "flecha izquierda": '←', "flecha derecha": '→'}
    
    key_stack = []
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key_name = event.name
            if key_name in arrows:
                key_stack.append(arrows[key_name])
            else:
                key_stack.append(key_name)
            
            if len(key_stack) > 10:
                del key_stack[0]
        
        if key_stack == konami_code:
            print("Konami code has been entered!!")
            break

        if keyboard.is_pressed('q'):
            break
        

if __name__ == "__main__":
    main()