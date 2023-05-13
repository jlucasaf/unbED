
entrada = int(input())
pilha_de_cartas = []
carta_retirada_string = ""
pares = []
impares = []
while entrada:
    for i in range(entrada):
        pilha_de_cartas.append(i + 1)
    pilha_de_cartas.sort(reverse=True)

    while len(pilha_de_cartas) > 1:
        carta_retirada = pilha_de_cartas.pop()

        if carta_retirada % 2:
            impares.append(carta_retirada)
        else:
            pares.append(carta_retirada)

        pilha_de_cartas.insert(0, pilha_de_cartas.pop())
        impares.sort()
        pares.sort(reverse=True)

    for i in impares:
        carta_retirada_string += str(i) + ", "
    for i in pares:
        carta_retirada_string += str(i) + ", "
    carta_retirada_string = carta_retirada_string[:-2]



    print("Discarded cards: " + carta_retirada_string)
    print("Remaining card: " + str(pilha_de_cartas[0]))
    pilha_de_cartas.clear()
    carta_retirada_string = ""
    pares.clear()
    impares.clear()
    entrada = int(input())