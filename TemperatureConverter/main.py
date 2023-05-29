"""
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
"""
#°F = (°C × 9/5) + 32
#°C = (°F − 32) x 5/9 
def temperature_converter(input_temp):
    try:
        parts = input_temp.replace(' ', '').split('°')
        
        if len(parts) == 2:
            if parts[1] == 'C':
                return f"{(float(parts[0]) * (9/5)) + 32}°F"

            return f"{(float(parts[0]) - 32) * (5/9)}°C"

        raise Exception()
    except:
        return "ERROR: Invalid input! For example, a valid format is: '100°C'"

def main():
    print(temperature_converter("100°C"))
    print(temperature_converter("100°F"))
    print(temperature_converter("100C"))
    print(temperature_converter("100F"))
    print(temperature_converter("100"))
    print(temperature_converter("100"))
    print(temperature_converter("- 100 °C "))
    print(temperature_converter("- 100 °F "))
    print(temperature_converter("100A°C"))
    print(temperature_converter("100A°F"))
    print(temperature_converter("°C"))
    print(temperature_converter("°F"))

if __name__ == "__main__":
    main()