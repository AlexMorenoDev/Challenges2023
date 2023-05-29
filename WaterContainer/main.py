"""
 * Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades
 * de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *          ⏹
 *          ⏹
 *   ⏹💧💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua.
 *   Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.
"""

def calculate_water_units(array):
    units = 0
    length = len(array)
    for i in range(length):
        if i > 0 and i < (length - 1):
            if array[i] < array[i-1] and array[i] < array[i+1]:
                if array[i-1] != array[i+1]:
                    units += min(array[i-1], array[i+1]) - array[i]
                    array[i] += min(array[i-1], array[i+1]) - array[i]
                else:
                    units += array[i+1] - array[i]
                    array[i] += array[i+1] - array[i]
        elif i == 0:
            if array[i] < array[i+1]:
                units += array[i+1] - array[i]
                array[i] = array[i+1] - array[i]
        else:
            if array[i] < array[i-1]:
                units += array[i-1] - array[i]
                array[i] = array[i-1] - array[i]
    
    lowest = 0
    greatest = 0
    pos_list = []
    for i in range(length):
        current = array[i]
        if current >= greatest:
            lowest = greatest
            greatest = current
            pos_list.append(i)

        if len(pos_list) == 2:
            for i in range(pos_list[0]+1, pos_list[1]):
                if array[i] < lowest:
                    units += lowest - array[i]
            
            pos_list = [pos_list[1]]


    return units

def main():
    # Probar con el segundo de aquí: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/pull/1039/files
    # Falta corregir ese caso
    array = [3, 1, 6, 3, 0, 4]
    print(calculate_water_units(array))
    

if __name__ == '__main__':
    main()