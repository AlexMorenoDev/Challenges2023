"""
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
"""

def is_decimal(val):
    if '.' in val and val.count('.') == 1 and val.replace('.', '').isnumeric():
        return True
    return False


def is_negative(val):
    num = val[1:]
    if val[0] == '-' and (num.isnumeric() or is_decimal(num)):
        return True
    return False


# 'expr': string
# 'valid_op': set containing valid operations
def is_math_expr(expr, valid_op):
    if len(expr) == 0:
        return "ERROR: Entered expression cannot be empty!"
    
    parts = expr.split(' ')

    num_count = 0
    sign_count = 0
    count = 0
    for el in parts:
        if el.isnumeric() or is_negative(el) or is_decimal(el):
            num_count += 1
        elif el in valid_op:
            sign_count += 1
        else:
            return False
        
        if (sign_count != num_count) and (sign_count != (num_count-1)):
            return False
    
        count += 1
    
    if sign_count == num_count:
        return False
    return True


def main():
    valid_op = {'+', '-', '*', '/', '%'}
    
    print(is_math_expr("5 + 6 / 7 - 4", valid_op)) # True
    print(is_math_expr("5 a 6", valid_op)) # False
    print(is_math_expr("51111 % 623 * 18000 % 400", valid_op)) # True
    print(is_math_expr("51111 * 0.23", valid_op)) # True
    print(is_math_expr("23 * 10 - 23 + -12 - 23 / 1", valid_op)) # True
    print(is_math_expr("23 * 10 - 23.2 + -12.522 - 23 / 1", valid_op)) # True
    print(is_math_expr("23 * 10..2 % 13.5", valid_op)) # False
    print(is_math_expr("23 * 10 - 23 /", valid_op)) # False
    print(is_math_expr("5 * 6 as", valid_op)) # False
    print(is_math_expr("b - c * a - w", valid_op)) # False
    print(is_math_expr("1 -- 2 / 3", valid_op)) # False
    print(is_math_expr("", valid_op)) # Error


if __name__ == "__main__":
    main()
