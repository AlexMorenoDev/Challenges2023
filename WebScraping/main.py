"""
 * Crea un programa que se conecte a la web del evento (https://holamundo.day)
 * e imprima únicamente la agenda de eventos del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
"""
import requests
from bs4 import BeautifulSoup


def main():
    webpage = requests.get("https://holamundo.day")
    soup = BeautifulSoup(webpage.content, "html.parser")

    block_elements = soup.find_all("blockquote")
    for element in block_elements[21:]:
        print(element.text)


if __name__ == "__main__":
    main()