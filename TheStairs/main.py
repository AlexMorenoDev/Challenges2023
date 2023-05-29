"""
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
"""

def draw_stairs(steps):
    floor = "_"
    
    if steps == 0:
        print(floor*2)
    elif steps > 0:
        steps += 1
        for i in reversed(range(steps)):
            n_spaces = i * 2
            if i == (steps-1):
                print((n_spaces*' ') + floor)
            else:
                print((n_spaces*' ') + "_|")
    else: 
        steps -= 1
        n_spaces = 0
        for i in range(abs(steps)):
            if i == 0:
                print((n_spaces*' ') + floor)
                n_spaces += 1
            else:
                print((n_spaces*' ') + "|_")
                n_spaces += 2
    

def main():
    draw_stairs(0)
    draw_stairs(10)
    draw_stairs(2)
    draw_stairs(-4)
    draw_stairs(-9)


if __name__ == "__main__":
    main()