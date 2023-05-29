''' 
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
'''

def get_url_params(url):
    params = url.split('?')[1].split('&')

    params_values = []
    for el in params:
        parts = el.split('=')
        params_values.append(parts[1])

    return params_values

def main():
    print(get_url_params("https://retosdeprogramacion.com?year=2023&challenge=0"))
    print(get_url_params("https//www.domain.com/page?key1=value1&key2=value2&key3=value3"))
    print(get_url_params("https//www.domain.com/page?key1=test"))
    

if __name__ == "__main__":
    main()