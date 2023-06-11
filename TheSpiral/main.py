"""
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗                        
 * ╔══╗║                                 
 * ║╔╗║║                        
 * ║╚═╝║                        
 * ╚═══╝                        
"""
from math import floor


def draw_spiral(n):
    i = n
    l = i - 1 
    l_c = 0
    r_w = 0
    l_w = 0
    
    # First half
    while i > floor(n/2):
        print(('║'*l_w) + ('╔'*l_c) + ('═'*l) + '╗' + ('║'*r_w))
        if r_w == 0:
            l_c = 1
        
        i -= 1
        l -= 2
        r_w += 1
        l_w = r_w - 1
    
    if n % 2 == 0:
        l = 0
    else:
        r_w -= 1
        l = 1
        
    # Second half
    for i in range(floor(n/2)):
        r_w -= 1
        print(('║'*r_w) + ('╚'*l_c) + ('═'*l) + '╝' + ('║'*r_w))
        l += 2
        
        
def main():
    draw_spiral(1)
    draw_spiral(5)
    draw_spiral(6)
    draw_spiral(12)
    draw_spiral(15)


if __name__ == '__main__':
    main()