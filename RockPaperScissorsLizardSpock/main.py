"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades
"""
win_conditions = {
    "🗿": ["✂️", "🦎"], 
    "✂️": ["📄", "🦎"],
    "📄": ["🗿", "🖖"],
    "🦎": ["🖖", "📄"],
    "🖖": ["✂️", "🗿"]
}

def rpsls(lst):
    p1_points = 0
    p2_points = 0
    for pair in lst:
        p1_move = pair[0]
        p2_move = pair[1]
        if p1_move != p2_move:
            if p2_move in win_conditions[p1_move]:
                p1_points += 1
            else:
                p2_points += 1

    if p1_points > p2_points:
        return "Player 1"
    if p2_points > p1_points:
        return "Player 2"
    return "Tie"


def main():
    print(rpsls([("🗿", "🗿")]))
    print(rpsls([("🗿", "✂️")]))
    print(rpsls([("✂️", "🗿")]))
    print(rpsls([("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")]))
    print(rpsls([("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")]))

if __name__ == "__main__":
    main()