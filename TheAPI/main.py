'''
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal o un archivo.
'''

import json, requests


def api_call():
    pokemon = "rayquaza"
    url =  f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
    res = requests.get(url)
    res_json = res.json()

    with open(f'{pokemon}.json', 'w', encoding='utf-8') as json_file:
        json.dump(res_json, json_file, indent=4)


def main():
    api_call()
    

if __name__ == "__main__":
    main()