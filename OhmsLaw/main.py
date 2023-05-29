"""
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
"""

# Conditions are set in this way "if i != None ..." because "if i ..." checks if i is None or 0
def ohm_law(v=None, r=None, i=None):
    if (i != None) and (r != None) and (v == None):
        return i * r
    elif (v != None) and (i != None) and (r == None):
        try:
            return v / i
        except ZeroDivisionError:
            return float('inf')
    elif (v != None) and (r != None) and (i == None):
        try:
            return v / r
        except ZeroDivisionError:
            return float('inf')
        
    return "Invalid values!"
    
def main():
    print(ohm_law())
    print(ohm_law(v = 5.0))
    print(ohm_law(v = 5.0, r = 4.0))
    print(ohm_law(v = 5.0, i = 4.0))
    print(ohm_law(r = 5.0, i = 4.0))
    print(ohm_law(v = 5.125, r = 4.0))
    print(ohm_law(v = 5.0, i = 4.125))
    print(ohm_law(r = 5.0, i = 4.125))
    print(ohm_law(v = 5.0, r = 0.0))
    print(ohm_law(v = 5.0, i = 0.0))
    print(ohm_law(r = 5.0, i = 0.0))
    print(ohm_law(v = 5.0, r = 4.0, i = 3.0))

if __name__ == "__main__":
    main()