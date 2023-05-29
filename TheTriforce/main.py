"""
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula: 2n-1.
 *
 * Ejemplo: Trifuerza 2
 *
 *     *
 *    ***
 *   *   *
 *  *** ***
"""

def draw_triforce(n):
    line_length = (2*n)-1

    triangle_lines = []
    # Calculate triangle lines
    for i in range(n):
        triangle_lines.append((' '*i)+ '*'*line_length + (' '*i))
        line_length -= 2

    # Draw top triangle
    for line in reversed(triangle_lines):
        print((' '*n) + line)

    # Draw bottom triangles
    for line in reversed(triangle_lines):
        print(line + ' ' + line)


def main():
    draw_triforce(2)
    draw_triforce(5)
    draw_triforce(10)


if __name__ == "__main__":
    main()
