from collections import deque

while True:
    n = int(input())

    if n == 0:
        break

    # Cria uma deque com as cartas de 1 a n
    cartas = deque(range(1, n+1))

    # Descarta a primeira carta
    descartadas = []
    while len(cartas) > 1:
        descartada = cartas.popleft()
        descartadas.append(descartada)

        # Move a nova carta do topo para o fundo, se houver
        if len(cartas) > 0:
            carta_topo = cartas.popleft()
            cartas.append(carta_topo)

    # Imprime a sequência de cartas descartadas
    print("Discarded cards: " + ", ".join(map(str, descartadas)))
    print("Remaining card: " + str(cartas[0]))